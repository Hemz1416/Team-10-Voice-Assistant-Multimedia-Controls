# Functional Test Cases — Voice Assistant

## 1. Purpose

Verify that the voice assistant recognizes supported multimedia commands, handles input variations and invalid requests, passes valid intents to the media controller, and reports execution failures appropriately.

## 2. Test Environment

- Test framework: pytest
- Test approach: automated tests with mocked media components where practical
- Original baseline before adding functional tests: 51 tests passed
- Full test suite after adding functional tests: 66 tests passed, 0 failed
- New automated functional tests added: 15
- Hardware-dependent microphone tests must be executed separately on the target machine.

## 3. Functional Test Cases

**Status definitions:** Pass = observed result matches expected result; Fail = observed result differs; Pending = not yet executed or requires unavailable hardware.

| Test ID | Input / Preconditions | Expected Result | Actual Result | Status |
|---|---|---|---|---|
| FT-01 | Input: `play` | Intent is `PLAY`; accepted command reaches the controller. | Covered by new automated test; passed. | Pass |
| FT-02 | Input: `pause` | Intent is `PAUSE`; accepted command reaches the controller. | Covered by new automated test; passed. | Pass |
| FT-03 | Input: `resume playback` | Intent is `RESUME`; accepted command reaches the controller. | Covered by new automated test; passed. | Pass |
| FT-04 | Input: `stop` | Intent is `STOP`; accepted command reaches the controller. | Covered by new automated test; passed. | Pass |
| FT-05 | Input: `next song` | Intent is `NEXT`; accepted command reaches the controller. | Covered by new automated test; passed. | Pass |
| FT-06 | Input: `previous track` | Intent is `PREVIOUS`; accepted command reaches the controller. | Covered by new automated test; passed. | Pass |
| FT-07 | Input: `volume up` | Intent is `VOLUME_UP`; accepted command reaches the controller. | Covered by new automated test; passed. | Pass |
| FT-08 | Input: `volume down` | Intent is `VOLUME_DOWN`; accepted command reaches the controller. | Covered by new automated test; passed. | Pass |
| FT-09 | Input: `mute` | Intent is `MUTE`; accepted command reaches the controller. | Covered by new automated test; passed. | Pass |
| FT-10 | Input: `  PLAY MUSIC  ` | Whitespace and case variations are handled; intent is `PLAY`. | Existing related test passes. | Pass |
| FT-11 | Input: `could you please play music` | Supported polite phrase maps to `PLAY`. | Existing related test passes. | Pass |
| FT-12 | Input: `can you pause music` | Supported polite phrase maps to `PAUSE`. | Existing related test passes. | Pass |
| FT-13 | Input: `turn the volume up` | Phrase maps to `VOLUME_UP`. | Existing related test passes. | Pass |
| FT-14 | Input: `turn the volume down` | Phrase maps to `VOLUME_DOWN`. | Existing related test passes. | Pass |
| FT-15 | Input: `please mute audio` | Phrase maps to `MUTE`. | Existing related test passes. | Pass |
| FT-16 | Input: empty string | No valid intent is returned; no media action executes. | Existing intent test passes; the new functional test also confirms no controller call for empty input. | Pass |
| FT-17 | Input: `open a browser` | Unsupported input is rejected; no media action executes. | Existing recognition test and new functional test pass. | Pass |
| FT-18 | Input: `dont play music` | Negated command is not treated as `PLAY`. | Existing related test passes; new functional test confirms no controller call. | Pass |
| FT-19 | Input: `play music and stop` | Conflicting command phrase is rejected rather than executing either action. | Existing related test passes; new functional test confirms no controller call. | Pass |
| FT-20 | Valid command with confidence below the configured threshold | Command is rejected and controller is not called. | Existing security/NFR tests pass. | Pass |
| FT-21 | Validated command with a controller exception | Service returns a failure result without propagating the exception to the caller. | Existing security/NFR tests pass. | Pass |
| FT-22 | Controller returns malformed response | Service rejects the response and reports an error result. | Existing command-service and security/NFR tests pass. | Pass |
| FT-23 | Play command with an empty playlist | Playback fails with an informative status; application does not crash. | Not yet tested separately. | Pending |
| FT-24 | Play command when VLC is unavailable | Failure is reported clearly; application does not crash. | Existing integration coverage includes a controller-unavailable volume operation; play-specific behavior is not separately verified here. | Pending — play-specific |
| FT-25 | Next command at the last playlist track | Playlist advances according to the documented wrap-around behavior. | Not yet tested separately. | Pending |
| FT-26 | Previous command at the first playlist track | Playlist moves to the last track according to the documented wrap-around behavior. | Not yet tested separately. | Pending |
| FT-27 | Volume up at maximum volume | Volume remains within 0–100%; no overflow occurs. | Not yet tested separately. | Pending |
| FT-28 | Volume down at minimum volume | Volume remains within 0–100%; no underflow occurs. | Not yet tested separately. | Pending |
| FT-29 | Mute command followed by another mute command | Mute state toggles on the first command and off on the second, when the controller succeeds. | Not yet tested separately. | Pending |
| FT-30 | Speak a supported command through the microphone | Speech is transcribed and routed to the expected intent. | Requires physical microphone and speech model. | Pending — hardware |
| FT-31 | Silence or unrecognized speech through the microphone | No unintended media command executes; suitable feedback is provided. | Requires physical microphone and speech model. | Pending — hardware |
| FT-32 | Controller returns a playback or audio-operation failure | Assistant reports failure clearly and does not claim the action succeeded. | General controller failure handling is tested; all media-specific failure cases are not yet verified. | Pending — additional coverage |

## 4. Execution Notes

- The original test suite contained 51 tests, all of which passed before the additional functional tests were added.
- The new automated functional test file contains 15 test cases, all of which passed.
- The full test suite was subsequently executed: **66 passed, 0 failed**.
- A recognition-only test does not prove that the controller was never called. The command pipeline must also be tested to verify this behavior.
- The automated functional tests use a fake media controller to verify command routing without requiring actual media playback.
- Microphone and real-device tests remain pending until they are executed on the target hardware.
- Playlist boundaries, volume limits, mute toggling, and all media-specific failure scenarios require additional testing.
- Actual results and statuses should be updated when the pending cases are executed.

## 5. Test Summary

| Metric | Result |
|---|---|
| Original automated tests | 51 |
| Original tests passed | 51 |
| Original tests failed | 0 |
| New automated functional tests | 15 |
| New functional tests passed | 15 |
| New functional tests failed | 0 |
| Total automated tests after additions | 66 |
| Total tests passed | 66 |
| Total tests failed | 0 |
| Documented functional test cases | 32 |
| Functional cases still pending or requiring additional coverage | FT-23, FT-24 (play-specific), FT-25 to FT-32 |
| Hardware-dependent tests | Pending |

**Conclusion:** All 66 automated tests passed. The automated suite verifies supported command routing, rejection of invalid or ambiguous input, and controller failure handling. The pending test cases require additional targeted tests or execution with the actual microphone and media environment. Passing the automated suite does not mean that every documented functional case has been independently executed.
