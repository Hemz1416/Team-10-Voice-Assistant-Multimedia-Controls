# System Validation Report

## 1. Project Information

| Field | Value |
|---|---|
| Project | Team 10 – Voice Assistant for Multimedia Controls |
| Report | System Validation Report |
| Test cycle | Sprint 2 / Final evaluation |
| Execution date | 2026-11-03 |
| Execution environment | Windows, Python 3.11.9, pytest 9.1.1 |

## 2. Objective

System validation checks whether the functional command flow correctly interprets supported commands, rejects unsupported or ambiguous input, passes validated commands to the media-control layer, and reports controller failures without treating them as successful actions.

## 3. Test Scope

| Test file | Scope | Test cases passed |
|---|---|---:|
| `tests/test_functional_commands.py` | Supported commands, rejection of unsupported/ambiguous inputs, and controller-failure reporting | 15 |
| `tests/test_media_integration.py` | Intent processing, validation, command service, media-controller integration behavior, and error handling | 4 |
| **Total** | | **19** |

**Execution command:**

```cmd
python -m pytest tests/test_functional_commands.py tests/test_media_integration.py -v
```

## 4. Validation Results

| Result | Count |
|---|---:|
| Passed | 19 |
| Failed | 0 |
| Errors | 0 |
| Skipped | 0 |
| Execution time | 0.20 seconds |

**Outcome: PASS for the automated functional/system-validation scenarios executed.**

## 5. Core Use-Case Results

| Validation area | Evidence in tests | Result |
|---|---|---|
| Supported media commands | Nine supported commands: PLAY, PAUSE, RESUME, STOP, NEXT, PREVIOUS, VOLUME_UP, VOLUME_DOWN, and MUTE | Passed |
| Unsupported or ambiguous input | Five invalid or ambiguous phrases are checked to ensure the controller is not called | Passed |
| Controller failure handling | A failed controller operation is returned as an unsuccessful command result | Passed |
| Play integration path | A validated PLAY intent reaches the media-controller implementation | Passed |
| Low-confidence protection | A low-confidence PLAY command is rejected and does not start playback | Passed |
| Volume integration path | A validated volume-up command reaches the controller | Passed |
| Unavailable controller handling | Controller failure is returned as an unsuccessful result | Passed |

## 6. Test Environment and Interpretation

The tests were executed on Windows using Python 3.11.9 and pytest 9.1.1.

The integration tests validate the software command flow and media-controller integration using a simulated VLC interface. They do not establish successful playback through a physical VLC installation or verify a live microphone/audio-device session.

The team has separately recorded Sprint 1 and Sprint 2 product demonstration videos in the repository:

- `docs/demo/videos/Team10_Sprint1_DemoVideo.mp4`
- `docs/demo/videos/Team10_Sprint2_Demovideo.mp4`

Those videos are supplementary manual demonstration evidence and were not re-recorded or independently re-evaluated as part of this automated test run.

## 7. Remaining Validation Limits

The following are not established by these 19 automated test cases:

- Live microphone capture and speech recognition accuracy against a defined dataset.
- End-to-end time from spoken command to media action and feedback.
- Actual VLC playback and audio output on the target Windows setup during this report run.
- Startup-time target and two-hour continuous-operation target.
- Audio retention/privacy behavior and complete application-level access controls.

These areas must remain marked as not verified until separate evidence is collected.

## 8. Conclusion

All 19 automated functional/system-validation test cases passed, with no failures, errors, or skips. The execution completed in 0.20 seconds. The tests provide evidence for supported command routing, rejection of unsupported or ambiguous commands, low-confidence protection, media-controller integration, and controller error handling. They do not constitute proof that every system-level or non-functional requirement has been met on the target hardware.