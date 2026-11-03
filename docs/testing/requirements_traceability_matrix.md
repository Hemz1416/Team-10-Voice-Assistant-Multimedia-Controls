# Requirements Traceability Matrix (RTM)

## Project Details
- **Project:** Team 10 – Voice Assistant for Multimedia Controls
- **Sprint:** Sprint 2 – Product and Testing
- **Purpose:** Map project requirements to test cases and record their execution status.

## 1. Traceability Matrix

| Requirement ID | Requirement | Related Test Case / Test Area | Actual Result | Status |
|---|---|---|---|---|
| REL-01 | Repeated command execution should be handled | Repeated command execution test | Test passed | Passed |
| REL-02 | Multiple supported intents should be handled | Supported intents test | Test passed | Passed |
| REL-03 | Controller should recover after failure | Controller recovery test | Test passed | Passed |
| REL-04 | Repeated controller failures should be handled | Repeated controller failure test | Test passed | Passed |
| SEC-01 | Unsupported or dangerous intents should be rejected | Parametrized unsupported intent tests | Test passed | Passed |
| SEC-02 | Rejected intents should not reach the controller | Rejected intent execution test | Test passed | Passed |
| SEC-03 | Invalid confidence should prevent execution | Invalid confidence test | Test passed | Passed |
| SEC-04 | Internal exception details should not be exposed | Exception handling test | Test passed | Passed |
| NFR-01 | Command-service execution time should be measurable | Command-service timing test | 0.009 ms observed | Recorded |
| NFR-02 | Full application startup should meet performance expectations | Application startup test | Not measured | Not Run |
| NFR-03 | Voice command response should meet latency expectations | End-to-end latency test | Not measured | Not Run |
| NFR-04 | Speech recognition should achieve acceptable accuracy | Speech recognition accuracy test | Not measured | Not Run |
| PRIV-01 | Raw microphone audio handling should protect user privacy | Audio privacy test | Not verified | Not Run |
| PRIV-02 | Sensitive information should not be exposed in logs | Log privacy test | Not verified | Not Run |
| SEC-05 | Application file permissions should be appropriate | File permission test | Not verified | Not Run |
| SEC-06 | Unauthorized access should be prevented | Access-control test | Not verified | Not Run |

## 2. Execution Summary

The additional automated test file `tests/test_additional_security_nfr.py` completed with:

- Total test executions: 13
- Passed: 13
- Failed: 0

These results apply only to the test scenarios covered by that file.

## 3. Pending Verification

The following areas require additional testing:

1. Full application startup performance.
2. End-to-end voice command latency.
3. Speech recognition accuracy.
4. Microphone audio storage and privacy.
5. Sensitive information in application logs.
6. Application file permissions.
7. Unauthorized access prevention.
8. Complete application-level reliability.

## 4. Traceability Status

Requirements marked **Passed** have corresponding passing automated test evidence from the additional test file.

Requirements marked **Recorded** have a measurement but do not yet have an established pass/fail threshold.

Requirements marked **Not Run** have not been verified. They must not be treated as passed.

## 5. Conclusion

The RTM connects selected reliability and security requirements to the available automated tests. Additional functional, performance, security, and privacy testing is required to complete traceability for the final release.