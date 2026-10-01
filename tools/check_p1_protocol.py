# -*- coding: utf-8 -*-
"""P1 incoming-letter protocol static check (mod side + joint app/mod checks).

Runs the structural checks that cannot live in the app repository's Jest
suite because they read CK3 mod files. Roots are passed EXPLICITLY; if a root
is missing the joint checks report "SKIPPED" instead of passing vacuously.

Usage:
    python tools/check_p1_protocol.py --mod-root <mod repo root> \
        --app-root <app repo root> [--generator <path relative to app root>]

Checks:
  1. UTF-8 BOM (EF BB BF) on every CK3-parsed text file touched by P1.
  2. Balanced braces on P1 CK3 script/GUI files.
  3. Every mod-prefixed scripted effect / trigger called by P1 files is
     defined inside this mod tree; P1 names are defined exactly once.
  4. on_action hooks follow the cross-file merge rules (events/on_actions
     blocks only; war-start uses the mod-owned relay; probe uses the v3
     gamedata entry).
  5. Great Project context lines exist for ordinary slots 1-6 with the full
     fact set; slots 7/8 never carry great_project_report.
  6. Slots 1-8 event/widget/run-file naming is consistent.
  7. Localization: no duplicate keys per language; bridge wire values are
     identical across all languages; P1 loc keys referenced by GUI/event/
     decision attributes exist in english and simp_chinese.
  8. Joint (needs --app-root): the app generator's VALID_TYPES are all covered
     by mod TYPE paths.
"""
import argparse
import io
import os
import re
import sys

CK3_P1_FILES = [
    'common/on_action/votc_incoming_letter_on_actions.txt',
    'common/scripted_effects/votc_incoming_letter_effects.txt',
    'common/scripted_effects/log_incoming_letter_gamedata_effect.txt',
    'common/scripted_triggers/votc_incoming_letter_triggers.txt',
    'events/votc_incoming_letter_events.txt',
    'common/decisions/votc_incoming_letter_settings.txt',
    'events/votc_incoming_letters_settings_bridge_events.txt',
    'common/scripted_guis/votc_incoming_letters.txt',
    'gui/custom_gui/votc_incoming_letters_window.gui',
    'gui/event_window_widgets/event_window_widget_letters_settings_opener.gui',
] + [f'gui/event_window_widgets/event_window_widget_incoming_letter_{i}.gui' for i in range(1, 9)]

LOC_LANGS = ['english', 'french', 'german', 'japaneese', 'korean', 'polish', 'russian', 'simp_chinese', 'spanish']
LOC_SUFFIX = {'japaneese': 'japanese'}

VALID_TYPES = [
    'vassal_memorial', 'siege_report', 'lost_holding', 'family_letter', 'poetry_letter',
    'courtier_petition', 'rival_taunt', 'dear_friend_greeting', 'letter_to_travelling_player',
    'ally_call_for_aid', 'revolt_urgent', 'deathbed_letter', 'pilgrimage_tales',
    'tour_tales', 'wedding_tales', 'hunt_tales', 'tournament_tales', 'travel_tales',
    'faction_warning', 'scheme_exposed', 'natural_disaster', 'tributary_letter',
    'liege_overlord_letter', 'great_work_notice', 'great_project_report',
]

GP_FACTS = ['sender_location', 'project_name', 'project_type', 'project_stage',
            'project_location', 'project_progress', 'project_days_left',
            'project_required_funded', 'project_required_total', 'project_founder',
            'project_owner', 'reporter_role', 'player_project_role']

errors = []
notes = []


def err(msg):
    errors.append(msg)


def read(p):
    with io.open(p, encoding='utf-8-sig', newline='') as f:
        return f.read()


def strip_comments_quotes(content):
    no_quotes = re.sub(r'"(?:[^"\\]|\\.)*"', '""', content)
    return '\n'.join(re.sub(r'#.*$', '', line) for line in no_quotes.split('\n'))


def brace_balance(content):
    depth = 0
    for ch in strip_comments_quotes(content):
        if ch == '{':
            depth += 1
        elif ch == '}':
            depth -= 1
        if depth < 0:
            return False
    return depth == 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--mod-root', required=True)
    ap.add_argument('--app-root', default=None)
    ap.add_argument('--generator', default='src/main/letter/IncomingLetterGenerator.ts')
    args = ap.parse_args()
    mod_root = args.mod_root

    contents = {}
    for rel in CK3_P1_FILES:
        p = os.path.join(mod_root, rel)
        if not os.path.exists(p):
            err(f'missing P1 file: {rel}')
            continue
        contents[rel] = read(p)

    # 1. BOM
    for rel in CK3_P1_FILES:
        p = os.path.join(mod_root, rel)
        if os.path.exists(p):
            with open(p, 'rb') as f:
                if f.read(3) != b'\xef\xbb\xbf':
                    err(f'file missing UTF-8 BOM: {rel}')
    for lang in LOC_LANGS:
        suf = LOC_SUFFIX.get(lang, lang)
        for base in ('clipboard_codes_l_%s.yml', 'talk_l_%s.yml'):
            p = os.path.join(mod_root, 'localization', lang, base % suf)
            if not os.path.exists(p):
                err(f'missing localization file: {p}')
                continue
            with open(p, 'rb') as f:
                if f.read(3) != b'\xef\xbb\xbf':
                    err(f'file missing UTF-8 BOM: localization/{lang}/{base % suf}')

    # 2. brace balance
    for rel, c in contents.items():
        if not brace_balance(c):
            err(f'unbalanced braces: {rel}')

    # 3. mod-prefixed reference closure
    p1_text = '\n'.join(contents.values())
    tree_texts = []
    for d in ('common', 'events', 'gui'):
        for root, _dirs, files in os.walk(os.path.join(mod_root, d)):
            for fn in files:
                if fn.endswith(('.txt', '.gui', '.info')):
                    try:
                        tree_texts.append(read(os.path.join(root, fn)))
                    except (OSError, UnicodeDecodeError):
                        pass
    tree_text = '\n'.join(tree_texts)

    defined_names = set(re.findall(r'^([a-zA-Z0-9_]+)\s*=\s*\{', p1_text, re.M))
    called = set(re.findall(r'^\s*([a-zA-Z0-9_]+)\s*=\s*yes\b', p1_text, re.M))
    for name in sorted(called):
        if not re.match(r'^(votc_|log_|mcc_)', name):
            continue  # vanilla triggers/effects are engine built-ins
        if name in defined_names:
            continue
        if re.search(r'^' + name + r'\s*=\s*\{', tree_text, re.M):
            continue
        err(f'P1 files call undefined effect/trigger: {name}')

    for name in sorted(defined_names):
        if name.startswith('votc_'):
            count = len(re.findall(r'^' + name + r'\s*=\s*\{', tree_text, re.M))
            if count > 1:
                err(f'effect/trigger/decision defined {count}x in tree: {name}')

    events_c = contents.get('events/votc_incoming_letter_events.txt', '')
    event_ids = re.findall(r'^votc_incoming_letter_event\.(\d+)\s*=\s*\{', events_c, re.M)
    if len(event_ids) != len(set(event_ids)):
        err('duplicate votc_incoming_letter_event ids')

    # 4. on_action merge rules
    on_actions = contents.get('common/on_action/votc_incoming_letter_on_actions.txt', '')
    m = re.search(r'on_war_started\s*=\s*\{([^}]*)\}', on_actions)
    if not m:
        err('on_war_started hook missing')
    else:
        if 'effect' in m.group(1):
            err('on_war_started must forward via on_actions, not define an effect block')
        if 'votc_war_started_incoming_letter_relay' not in m.group(1):
            err('on_war_started relay missing')
    for hook in ('quarterly_playable_pulse', 'on_army_monthly', 'on_siege_completion',
                 'on_death', 'on_travel_plan_complete', 'on_building_started',
                 'on_building_completed'):
        if hook not in on_actions:
            err(f'on_action hook missing: {hook}')
    if 'votc_incoming_letter_event.9001' not in events_c:
        err('.9001 probe event missing')
    if 'log_gamedata_v3 = yes' not in events_c:
        err('.9001 probe does not call log_gamedata_v3 (target v3 entry)')
    if re.search(r'^\s*log_gamedata\s*=\s*yes', events_c, re.M):
        err('.9001 still references the retired log_gamedata entry')

    # 5. great project facts on slots 1-6
    effects = contents.get('common/scripted_effects/votc_incoming_letter_effects.txt', '')
    gp_lines = re.findall(
        r'debug_log\s*=\s*"(VOTC:INCOMING_LETTER/;/context/;/incoming_letter_[1-6]/;/great_project_report[^"]*)"',
        effects)
    if len(gp_lines) != 6:
        err(f'expected 6 great_project_report context lines (slots 1-6), found {len(gp_lines)}')
    for slot in range(1, 7):
        line = next((l for l in gp_lines if f'/incoming_letter_{slot}/;/' in l), None)
        if line is None:
            err(f'no great_project_report context for slot {slot}')
            continue
        for field in GP_FACTS:
            if f'/;/{field}=' not in line:
                err(f'great_project_report slot {slot} missing fact {field}')
    for slot in (7, 8):
        if f'incoming_letter_{slot}/;/great_project_report' in effects:
            err(f'great_project_report must not use dedicated slot {slot}')

    # 6. slots 1-8 naming consistency
    for slot in range(1, 9):
        p = os.path.join(mod_root, f'gui/event_window_widgets/event_window_widget_incoming_letter_{slot}.gui')
        if not os.path.exists(p):
            err(f'missing widget for slot {slot}')
            continue
        widget = read(p)
        if f'run incomingletter_v2_{slot}.txt' not in widget:
            err(f'widget {slot} does not execute run incomingletter_v2_{slot}.txt')
    triggers = contents.get('common/scripted_triggers/votc_incoming_letter_triggers.txt', '')
    for slot in (7, 8):
        if f'incoming_letter_{slot}' not in triggers:
            err(f'triggers missing dedicated slot {slot}')
    for rel in ('common/scripted_guis/votc_incoming_letters.txt',
                'gui/custom_gui/votc_incoming_letters_window.gui'):
        if 'votc_battle_reports' in contents.get(rel, ''):
            err(f'battle-report coupling left in {rel}')

    # 7. localization
    bridge_values = {}
    cc_maps = {}
    talk_maps = {}
    for lang in LOC_LANGS:
        suf = LOC_SUFFIX.get(lang, lang)
        cc = read(os.path.join(mod_root, 'localization', lang, f'clipboard_codes_l_{suf}.yml'))
        tk = read(os.path.join(mod_root, 'localization', lang, f'talk_l_{suf}.yml'))
        cc_pairs = re.findall(r'^\s*([A-Za-z0-9_.]+):\d\s+"(.*)"\s*$', cc, re.M)
        tk_pairs = re.findall(r'^\s*([A-Za-z0-9_.]+):\d\s+"(.*)"\s*$', tk, re.M)
        cc_map = dict(cc_pairs)
        tk_map = dict(tk_pairs)
        if len(cc_map) != len(cc_pairs):
            err(f'duplicate keys in {lang} clipboard_codes')
        if len(tk_map) != len(tk_pairs):
            err(f'duplicate keys in {lang} talk')
        for i in range(1, 9):
            key = f'votc_incoming_letter_bridge_{i}'
            if key not in cc_map:
                err(f'{lang} clipboard_codes missing {key}')
            else:
                if key in bridge_values and bridge_values[key] != cc_map[key]:
                    err(f'bridge {key} differs between languages (wire payload must not be translated)')
                bridge_values[key] = cc_map[key]
        cc_maps[lang] = cc_map
        talk_maps[lang] = tk_map

    en = talk_maps.get('english', {})
    zh = talk_maps.get('simp_chinese', {})
    en_cc = cc_maps.get('english', {})
    loc_used = set()
    for c in contents.values():
        loc_used |= set(re.findall(r'(?:^|\s)(?:text|title|desc|tooltip|confirm_text)\s*=\s*(votc_[a-z0-9_]+)', c, re.M))
    for extra in ('votc_incoming_letter_fallback_desc', 'votc_incoming_letters_hud_button_tooltip'):
        if extra in p1_text:
            loc_used.add(extra)
    for key in sorted(loc_used):
        # Bridge keys resolve through clipboard_codes (wire payloads), all
        # other P1 keys through the talk files.
        if re.fullmatch(r'votc_incoming_letter_bridge_[0-9]', key):
            if key not in en_cc:
                err(f'P1 bridge key referenced but missing in english clipboard_codes: {key}')
            continue
        if key not in en:
            err(f'P1 loc key referenced but missing in english talk: {key}')
        if key not in zh:
            err(f'P1 loc key referenced but missing in simp_chinese talk: {key}')

    # 8. joint app checks (explicit root)
    if args.app_root:
        gen_path = os.path.join(args.app_root, args.generator)
        if os.path.exists(gen_path):
            gen = read(gen_path)
            for t in VALID_TYPES:
                if f"'{t}'" not in gen:
                    err(f'app generator missing type {t}')
                if f'flag:{t}' not in p1_text and t not in triggers:
                    err(f'mod side has no path for type {t}')
        else:
            notes.append(f'app generator not found at {gen_path}; joint type checks SKIPPED')
    else:
        notes.append('--app-root not given; joint app/mod type checks SKIPPED')

    for n in notes:
        print(f'NOTE: {n}')
    if errors:
        print(f'\nFAILED with {len(errors)} problem(s):')
        for e in errors:
            print(f'  [P1-CHECK] {e}')
        return 1
    print('P1 protocol static check: PASS')
    return 0


if __name__ == '__main__':
    sys.exit(main())
