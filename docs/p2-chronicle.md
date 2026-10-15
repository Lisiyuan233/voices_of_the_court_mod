# Court Chronicle (P2)

Adds the Court Chronicle decision, human-player quarterly/yearly events, memory snapshots and the 25-field desktop-app bridge. The pulse hooks only append `events`, so they merge with vanilla on_actions. Request ID, signal kind and quarter are captured in each event chain; simultaneous pulses cannot read a later request's global values. The signal kind is a flag scope (`save_scope_as`), while the request ID and quarter are numeric values (`save_scope_value_as`). The request ID remains in the positive 28-bit range.

The bridge emits the same payload through clipboard and `debug.log`. English and Simplified Chinese include translated player text; seven other mod languages carry English fallback text and identical bridge values. The ordinary v3/s/l snapshots gain the numeric game-date five-tuple needed by the historian, before the existing snapshot-protocol tail.

The log payload is emitted synchronously by the manager effect before it queues the clipboard event. Resolving the description through `Localize()` in `debug_log` loses saved event targets and produces empty request fields. The paired app accepts the log even when clipboard polling is enabled and deduplicates the two transports by campaign/player/request. The decision shows a translated tooltip instead of implementation details. Script triggers use `is_ai = no`; `is_local_player` is interface-only and cannot be used in these decision/event trigger blocks.

CK3 still evaluates hidden effects during tooltip dry runs without applying their assignments. Request captures therefore check that all three globals exist before reading them, avoiding unset-scope errors when previewing the decision before its first execution.

Use the paired P2 app, based on the release branch that contains P1. The mod metadata and binary assets are unchanged.

## Checks

```powershell
python tools/check_chronicle_protocol.py --mod-root . --app-root <paired-app-checkout>
python tools/check_p1_protocol.py --mod-root . --app-root <paired-app-checkout>
```

The P2 check covers BOM, balanced blocks, event/effect/localization references, pulse registrations, all nine localization bridges, numeric date fields and paired app protocol constants.

## Game acceptance

Install this checkout into an independent CK3 test mod directory, create its launcher `.mod` entry, enable that entry in a test playset and load a disposable save. Copy the two `run_test_scripts/votc_test_chronicle*.txt` scripts into CK3's `run` directory.

1. Start the paired app. Use the **Open Court Chronicle** decision to open the manager without generating automatically.
2. Run `run votc_test_chronicle.txt` or invoke the individual quarterly/yearly/manual effects from the console. Verify `VOTC:CHRONICLE_MEMORY` start/memory/participant/end records and the matching manager/tick request ID.
3. Generate an entry from a conversation, ordinary letter, incoming letter and player memory; verify dates, source text and the active timeline.
4. Disable automatic generation, then select quarterly/yearly in the app and verify matching pulses. Vanilla playable pulses are staggered by birthday; they are not calendar-boundary timers.
5. Retry a failed request, regenerate after late sources arrive, and load a sibling save. Material from an abandoned branch must stay hidden.
6. Stop clipboard listening in the app and repeat the manager request through the log bridge.
7. Leave clipboard listening enabled and repeat the decision. Verify that the log and clipboard copies open the window once, with a nonempty `manual` kind, quarter and request ID; the request ID must match its memory block. After updating an already-running game, restart CK3 before this check so it loads the modified decision/effect/event definitions.

The optional memory-identity script is a diagnostic probe for game API behavior; inspect its logs separately from the ordinary acceptance run. The automated checks cannot confirm that CK3 has loaded this test directory or executed these effects.
