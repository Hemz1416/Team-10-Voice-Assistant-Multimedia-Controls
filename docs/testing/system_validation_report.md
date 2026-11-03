# System Validation Report

## 1. Project Information

| Field | Value |
|---|---|
| Project | Team 10 – Voice Assistant for Multimedia Controls |
| Report | System Validation Report |
| Test cycle | Sprint 2 / Final evaluation preparation |
| Execution date | 2026-11-03 |
| Source snapshot | `73e7425` (source archive supplied for this report run) |
| Execution environment | Linux x86_64, Python 3.13.5, pytest 9.0.2 |

## 2. Objective

System validation checks whether the functional command flow correctly interprets supported commands, rejects unsupported or ambiguous input, passes validated commands to the media-control layer, and reports controller failures without treating them as successful actions.

## 3. Test Scope

| Test file | Scope | Test cases passed |
|---|---|---:|
| `tests/test_functional_commands.py` | Supported commands, rejection of unsupported/ambiguous inputs, and controller-failure reporting | 15 |
| `tests/test_media_integration.py` | Intent processing, validation, command service, media-controller integration behavior, and error handling | 4 |
| **Total** |  | **19** |

**Execution command:**

```bash
python -m pytest tests/test_functional_commands.py tests/test_media_integration.py -q
```

## 4. Validation Results

| Result | Count |
|---|---:|
| Passed | 19 |
| Failed | 0 |
| Errors | 0 |
| Skipped | 0 |
| Reported execution time | 0.06 seconds |

<text>**Outcome: PASS for the automated functional/system-validation scenarios executed.**</text>

## 5. Core Use-Case Results

| Validation area | Evidence in tests | Result |
|---|---|---|
| Supported media commands | Nine supported command phrases are checked, including PLAY, PAUSE, RESUME, STOP, NEXT, PREVIOUS, VOLUME_UP, VOLUME_DOWN, and MUTE | Passed |
| Unsupported or ambiguous input | Five empty, unsupported, or ambiguous phrases are checked to ensure that the controller is not called | Passed |
| Controller failure handling | A failed controller operation is returned as an unsuccessful command result | Passed |
| Play integration path | A validated PLAY intent reaches the media-controller implementation and updates the simulated playback state | Passed |
| Low-confidence protection | A low-confidence PLAY command is rejected and does not start playback | Passed |
| Volume integration path | A validated volume-up command reaches the controller and updates the simulated volume | Passed |
| Unavailable controller handling | Controller unavailability is returned as an unsuccessful result with a controlled status message | Passed |

## 6. Test Environment and Interpretation

The integration test file constructs a `MediaController` with a fake VLC instance, fake media object, and fake player. Consequently, these automated tests validate the software integration path and controller behavior against a simulated VLC interface. They do **not** establish successful playback through a physical VLC installation or verify a live microphone/audio-device session.

The team has separately recorded Sprint 1 and Sprint 2 product demonstration videos in the repository:

- `docs/demo/videos/Team10_Sprint1_DemoVideo.mp4`
- `docs/demo/videos/Team10_Sprint2_Demovideo.mp4`

Those videos are supplementary manual demonstration evidence. They were not re-recorded or independently re-evaluated as part of the automated test run documented here.

## 7. Remaining Validation Limits

The following are not established by the 19 automated test cases:

- Live microphone capture and speech recognition accuracy against a defined dataset.
- End-to-end time from spoken command to media action and feedback.
- Actual VLC playback and audio output on the target Windows setup during this report run.
- Startup-time target and two-hour continuous-operation target.
- Audio retention/privacy behavior and complete application-level access controls.

These areas must remain marked as not verified until separate evidence is collected.

## 8. Conclusion

All 19 automated functional/system-validation test cases passed. The tests provide evidence for supported command routing, rejection of unsupported or ambiguous commands, low-confidence protection, simulated media-controller integration, and controller error handling. They do not constitute proof that every system-level or non-functional requirement has been met on the target hardware.
