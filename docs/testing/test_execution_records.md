# Test Execution Records
## Voice Assistant for Multimedia Controls

**Project:** Team 10 – Voice Assistant for Multimedia Controls
**Sprint:** Sprint 2 – Product and Testing  
**Final test environment:** Windows, Python 3.11.9, pytest 9.1.1
**Execution date:** 2026-11-03

---

## 1. Objective

This document records the automated test executions performed during the project, including historical additional security testing and the later unit and system-validation test runs.

## 2. Test Execution Summary

| Test execution | Passed | Failed | Errors | Skipped | Duration |
|---|---:|---:|---:|---:|---:|
| Historical additional security/NFR tests | 13 | 0 | 0 | 0 | 0.09 sec |
| Final targeted unit tests | 93 | 0 | 0 | 0 | 0.69 sec |
| Final system-validation tests | 19 | 0 | 0 | 0 | 0.20 sec |

The 20 additional subtests reported in the unit-test execution are recorded separately and are not included in the 93 pytest test cases.

These are separate test executions. Their counts should not be interpreted as one combined pytest run.

## 3. Historical Additional Security/NFR Execution

**Test file:** `tests/test_additional_security_nfr.py`

**Command:**
```bash
python -m pytest tests/test_additional_security_nfr.py -v -s
```

**Environment:** Windows 10, Python 3.13.1, pytest 8.3.4.

**Result:** 13 passed, 0 failed, in 0.09 seconds.

This historical execution covered repeated command handling, controller recovery, unsupported-intent rejection, confidence validation, command-service timing, and exception handling.

## 4. Final Unit-Test Execution

**Test files:**
- `tests/test_command_service.py`
- `tests/test_command_validator.py`
- `tests/test_intent_processor.py`
- `tests/test_intent_variations.py`
- `tests/test_media_controller.py`
- `tests/test_security_nfr.py`

**Command:**
```cmd
python -m pytest tests/test_command_service.py tests/test_command_validator.py tests/test_intent_processor.py tests/test_intent_variations.py tests/test_media_controller.py tests/test_security_nfr.py -v
```

**Environment:** Windows, Python 3.11.9, pytest 9.1.1.

**Result:** 93 passed, 0 failed, 0 errors, 0 skipped, in 0.69 seconds. An additional 20 subtests passed.

## 5. Final System-Validation Execution

**Test files:**
- `tests/test_functional_commands.py`
- `tests/test_media_integration.py`

**Command:**
```cmd
python -m pytest tests/test_functional_commands.py tests/test_media_integration.py -v
```

**Environment:** Windows, Python 3.11.9, pytest 9.1.1.

**Result:** 19 passed, 0 failed, 0 errors, 0 skipped, in 0.20 seconds.

These tests cover supported command routing, rejection of unsupported and ambiguous input, low-confidence protection, media-controller integration behavior, and controller error handling.

The integration tests use a simulated VLC interface and do not independently establish physical audio output.

## 6. Separate Product Demonstration Evidence

The Sprint 2 demonstration script was also documented as executing the nine supported voice intents successfully on a native libVLC runtime.

The demonstration includes PLAY, PAUSE, RESUME, VOLUME_UP, VOLUME_DOWN, NEXT, PREVIOUS, MUTE, and STOP operations.

The recorded demonstration is supplementary product evidence, not an additional automated pytest execution.

## 7. Remaining Verification

The following areas have not been established by the recorded automated test runs:

- Formal speech-recognition accuracy measurement.
- Full application startup-time measurement.
- End-to-end microphone-to-response latency.
- User-feedback latency measurement.
- Two-hour continuous-operation reliability.
- Complete microphone audio privacy verification.
- Complete application-level file permission and access-control verification.

These requirements must remain marked as not verified until separate evidence is available.

## 8. Conclusion

The historical additional security/NFR execution passed 13 tests. The later targeted unit-test execution passed 93 pytest cases and 20 additional subtests. The later system-validation execution passed 19 cases.

All reported executions had zero failures. The results provide evidence for the tested component and software integration behavior. They do not establish that every performance, privacy, hardware, or non-functional requirement has been satisfied.