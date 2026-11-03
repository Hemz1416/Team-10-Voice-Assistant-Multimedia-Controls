# Requirements Traceability Matrix (RTM)

## Project Details

- **Project:** Team 10 – Voice Assistant for Multimedia Controls
- **Sprint:** Sprint 2 – Product and Testing
- **Purpose:** Map project requirements to available test evidence and record verification status.
- **Final targeted test environment:** Windows, Python 3.11.9, pytest 9.1.1

## 1. Traceability Matrix

| Requirement ID | Requirement | Related Test Evidence | Actual Result | Status |
|---|---|---|---|---|
| REL-01 | Repeated command execution should be handled | Additional security/NFR tests | Test passed | Passed |
| REL-02 | Multiple supported intents should be handled | Unit and system-validation tests | Test passed | Passed |
| REL-03 | Controller should recover after failure | Additional security/NFR tests | Test passed | Passed |
| REL-04 | Repeated controller failures should be handled | Additional security/NFR tests | Test passed | Passed |
| SEC-01 | Unsupported or dangerous intents should be rejected | Unit and additional security tests | Test passed | Passed |
| SEC-02 | Rejected intents should not reach the controller | Unit and system-validation tests | Test passed | Passed |
| SEC-03 | Invalid confidence should prevent execution | Unit and system-validation tests | Test passed | Passed |
| SEC-04 | Internal exception details should not be exposed | Additional security and unit tests | Tested scenarios passed | Passed |
| NFR-01 | Command-service execution time should be measurable | Additional security/NFR timing test | 0.009 ms observed | Recorded |
| NFR-02 | Full application startup should meet performance expectations | Application startup measurement | Not measured | Not Run |
| NFR-03 | Voice command response should meet latency expectations | End-to-end latency measurement | Not measured | Not Run |
| NFR-04 | Speech recognition should achieve acceptable accuracy | Speech recognition accuracy measurement | Not measured | Not Run |
| PRIV-01 | Raw microphone audio handling should protect user privacy | Audio privacy verification | Not verified | Not Run |
| PRIV-02 | Sensitive information should not be exposed in logs | Log privacy verification | Not verified | Not Run |
| SEC-05 | Application file permissions should be appropriate | File permission verification | Not verified | Not Run |
| SEC-06 | Unauthorized access should be prevented | Access-control verification | Not verified | Not Run |

## 2. Test Execution Evidence

The following separate automated executions are recorded:

| Execution | Test Scope | Passed | Failed | Duration |
|---|---|---:|---:|---:|
| Historical additional security/NFR run | `test_additional_security_nfr.py` | 13 | 0 | 0.09 sec |
| Final unit-test run | Six targeted unit-test files | 93 | 0 | 0.69 sec |
| Final system-validation run | Functional commands and media integration | 19 | 0 | 0.20 sec |

The unit-test run also reported 20 additional passing subtests, recorded separately from the 93 pytest cases.

The historical additional security/NFR execution used Windows 10, Python 3.13.1, and pytest 8.3.4. The later unit and system-validation executions used Windows, Python 3.11.9, and pytest 9.1.1.

## 3. Additional Product Demonstration Evidence

The Sprint 2 demonstration records successful execution of the nine supported voice intents using a native libVLC runtime:

- PLAY
- PAUSE
- RESUME
- STOP
- NEXT
- PREVIOUS
- VOLUME_UP
- VOLUME_DOWN
- MUTE

This demonstration is supplementary product evidence. It is separate from the automated test executions.

## 4. Pending Verification

The following areas remain unverified:

1. Full application startup performance.
2. End-to-end voice-command response latency.
3. Formal speech-recognition accuracy.
4. Raw microphone audio storage and privacy.
5. Sensitive information exposure in application logs.
6. Application file permissions.
7. Unauthorized access prevention.
8. Long-duration application reliability.

## 5. Traceability Status

- **Passed:** Corresponding automated test evidence is available for the tested scenario.
- **Recorded:** A measurement exists, but a pass/fail threshold has not been established.
- **Not Run:** The requirement has not been verified and must not be treated as passed.

The automated test results establish only the behavior covered by their respective test scopes. Simulated media-controller integration does not independently establish physical audio output or complete hardware-level operation.

## 6. Conclusion

The RTM connects the available reliability, functional, and security test evidence to the corresponding requirements.

The historical additional security/NFR execution passed 13 tests. The later unit-test execution passed 93 pytest cases and 20 additional subtests. The later system-validation execution passed 19 cases.

Performance, speech-recognition accuracy, privacy, application-level access control, and long-duration reliability requirements remain pending verification. These limitations are retained in the matrix to ensure accurate final evaluation reporting.