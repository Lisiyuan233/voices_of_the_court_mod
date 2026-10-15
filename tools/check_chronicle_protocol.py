"""Check the P2 CK3 files and, optionally, the paired app protocol.

python tools/check_chronicle_protocol.py --mod-root . --app-root <app checkout>
"""
import argparse
import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True
from check_p1_protocol import LOC_LANGS, LOC_SUFFIX, brace_balance, strip_comments_quotes


def check(mod: Path, app: Path | None):
    files = [
        'common/on_action/votc_chronicle_on_actions.txt',
        'common/scripted_effects/votc_chronicle_effects.txt',
        'common/decisions/votc_chronicle_decisions.txt',
        'events/votc_chronicle_events.txt',
        'run_test_scripts/votc_test_chronicle.txt',
        'run_test_scripts/votc_test_chronicle_memory_identity.txt',
        'common/scripted_effects/log_gamedata_v3_effect.txt',
        'common/scripted_effects/log_gamedata_v3s_effect.txt',
        'common/scripted_effects/log_gamedata_v3l_effect.txt',
    ]
    contents = {}
    for name in files:
        data = (mod / name).read_bytes()
        assert data.startswith(b'\xef\xbb\xbf'), f'Missing BOM: {name}'
        text = data.decode('utf-8-sig')
        assert brace_balance(text), f'Unbalanced script: {name}'
        contents[name] = text

    hooks = contents[files[0]]
    assert not re.search(r'^\s*(trigger|effect)\s*=', strip_comments_quotes(hooks), re.M)
    assert re.search(r'quarterly_playable_pulse\s*=\s*\{\s*events\s*=\s*\{\s*votc_chronicle_event\.9001', hooks)
    assert re.search(r'yearly_playable_pulse\s*=\s*\{\s*events\s*=\s*\{\s*votc_chronicle_event\.9002', hooks)
    effects = contents[files[1]]
    assert effects.count('name = votc_chronicle_request_snapshot') == 2
    assert effects.count('name = votc_chronicle_kind_snapshot') == 2
    assert effects.count('name = votc_chronicle_quarter_snapshot') == 2
    id_block = effects.split('votc_generate_chronicle_request_id_effect = {', 1)[1].split('\n}', 1)[0]
    assert id_block.count('votc_append_chronicle_request_id_bit_effect = yes') == 27
    events = contents[files[3]]
    for name in files[6:]:
        init = next(line for line in contents[name].splitlines() if 'VOTC:IN/;/init/;/' in line)
        fields = init.split('VOTC:IN/;/init/;/', 1)[1].split('/;/')
        assert len(fields) == 29 and 'GetDateAsTotalDays' in fields[23], f'Numeric game date missing: {name}'
    assert events.count('is_local_player = yes') == 4
    for number in (9003, 9004):
        assert f'debug_log = "[Localize(\'votc_chronicle_event.{number}.desc\')]"' in events
    assert events.count('event_window_widget_talk_clear') == 2

    # All invoked chronicle effects and events must resolve exactly once.
    definitions = {}
    for name in files[:4]:
        for key in re.findall(r'^(votc_chronicle_[\w.]+|votc_\w+_chronicle_\w+)\s*=\s*\{', contents[name], re.M):
            definitions[key] = definitions.get(key, 0) + 1
    for key, count in definitions.items():
        assert count == 1, f'Duplicate definition: {key}'
    for text in contents.values():
        for effect in re.findall(r'\b(votc_\w*chronicle\w*_effect)\s*=\s*yes', strip_comments_quotes(text)):
            assert definitions.get(effect) == 1, f'Unresolved effect: {effect}'
        for event in re.findall(r'\b(votc_chronicle_event\.\d+)\b', strip_comments_quotes(text)):
            assert definitions.get(event) == 1, f'Unresolved event: {event}'

    bridges = None
    for language in LOC_LANGS:
        suffix = LOC_SUFFIX.get(language, language)
        file = mod / f'localization/{language}/votc_chronicle_l_{suffix}.yml'
        data = file.read_bytes()
        assert data.startswith(b'\xef\xbb\xbf'), f'Missing localization BOM: {file}'
        text = data.decode('utf-8-sig')
        assert text.splitlines()[0] == f'l_{suffix}:'
        entries = re.findall(r'^\s*([\w.]+):0\s+"(.*)"\s*$', text, re.M)
        assert len(entries) == len({key for key, _ in entries}), f'Duplicate localization key: {file}'
        values = dict(entries)
        for key in re.findall(r'\b(?:title|desc|custom_tooltip)\s*=\s*(votc_\w[\w.]*)', events + contents[files[2]]):
            assert key in values, f'Unresolved localization: {key} ({language})'
        current = [values[f'votc_chronicle_event.{number}.desc'] for number in (9003, 9004)]
        for wire, command in zip(current, ('CHRONICLE_TICK', 'CHRONICLE_MANAGER')):
            segments = wire.split('/;/')
            assert len(segments) == 26 and segments[0] == f'VOTC:{command}'
            assert segments[10] == '2', 'Protocol schema must remain v2'
            assert "SCOPE.GetFlagName('votc_chronicle_kind_snapshot')" in segments[18]
            assert "SCOPE.GetValue('votc_chronicle_request_snapshot')" in segments[25]
        if bridges is None:
            bridges = current
        assert bridges == current, f'Bridge differs across languages: {language}'

    if app:
        parser = (app / 'src/main/chronicle/chronicleClipboardPayload.ts').read_text(encoding='utf-8')
        assert 'CHRONICLE_CLIPBOARD_FIELD_COUNT = 25' in parser
        listener = (app / 'src/main/ClipboardListener.ts').read_text(encoding='utf-8')
        assert 'readChronicleLogLine' in listener and 'CHRONICLE_TICK' in listener and 'CHRONICLE_MANAGER' in listener
        ipc = (app / 'src/main/ipc/chronicleIpc.ts').read_text(encoding='utf-8')
        assert 'waitForChronicleMemoryBlock' in ipc and 'memoryResult.playerId !== payload.playerId' in ipc
        print('PASS: paired app/mod payload and memory protocol')
    else:
        print('SKIPPED: paired app checks (--app-root was not supplied)')
    print(f'PASS: {len(files)} CK3 scripts, {len(LOC_LANGS)} localization sets, references, pulse hooks and BOM')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--mod-root', type=Path, required=True)
    parser.add_argument('--app-root', type=Path)
    args = parser.parse_args()
    check(args.mod_root.resolve(), args.app_root.resolve() if args.app_root else None)
