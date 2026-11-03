# Test Evidence Index

## Project Details
- **Project:** Team 10 – Voice Assistant for Multimedia Controls
- **Sprint:** Sprint 2 – Product and Testing
- **Purpose:** Maintain an organized list of test reports, automated test files, execution results, and supporting evidence.

## 1. Automated Test Evidence

| Evidence ID | Evidence Name | Location | Description | Availability |
|---|---|---|---|---|
| EV-01 | Additional Security and Reliability Tests | `tests/test_additional_security_nfr.py` | Automated security and reliability test cases | Available |
| EV-02 | Additional Test Execution Result | Terminal output | 13 passed, 0 failed in 0.09 seconds | Recorded |
| EV-03 | Command-Service Timing | Terminal output | Recorded command-service execution time of 0.009 ms | Recorded |

## 2. Testing Documentation

| Evidence ID | Document | Location | Purpose |
|---|---|---|---|
| DOC-01 | Test Execution Records | `docs/testing/test_execution_records.md` | Records test execution outcomes |
| DOC-02 | Defect Log | `docs/testing/defect_log.md` | Tracks identified defects |
| DOC-03 | Retest Records | `docs/testing/retest_records.md` | Records defect retesting |
| DOC-04 | Performance Metrics | `docs/testing/performance_metrics.md` | Records performance measurements |
| DOC-05 | Security and Privacy Report | `docs/testing/security_privacy_report.md` | Documents security and privacy testing |
| DOC-06 | Requirements Traceability Matrix | `docs/testing/requirements_traceability_matrix.md` | Maps requirements to test cases and results |
| DOC-07 | Final Test Summary Report | `docs/testing/final_test_summary_report.md` | Summarizes available test evidence |

## 3. Additional Evidence to Collect

The following evidence has not yet been recorded and should be added when the corresponding tests are executed:

- Full functional test execution output.
- Application startup timing results.
- End-to-end voice command response timing.
- Speech recognition accuracy results.
- Long-duration reliability test results.
- Microphone audio privacy verification.
- Application log privacy verification.
- File permission and access-control test results.
- Screenshots or logs for confirmed defects.
- Retest output after defect fixes.

## 4. Evidence Management Guidelines

1. Use unique evidence IDs.
2. Store evidence in the appropriate repository folder.
3. Include test names and execution dates where available.
4. Keep original test outputs whenever possible.
5. Link each evidence item to its related test case or requirement.
6. Update this index whenever new evidence is collected.
7. Do not mark pending evidence as available until it has actually been collected.

## 5. Current Evidence Status

The additional automated security and reliability test file and its reported execution output are currently available.

Other evidence items listed under additional evidence remain pending until the corresponding tests are performed.

## 6. Conclusion

This index provides a central reference for the Sprint 2 testing documents and currently available automated test evidence. It will be updated as additional testing and verification activities are completed.