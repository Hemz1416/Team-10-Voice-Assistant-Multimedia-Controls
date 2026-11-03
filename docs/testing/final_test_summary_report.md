# Final Test Summary Report

## 1. Project Details

- **Project:** Team 10 – Voice Assistant for Multimedia Controls
- **Sprint:** Sprint 2 – Product and Testing
- **Report Type:** Final Test Summary Report
- **Final targeted test environment:** Windows, Python 3.11.9, pytest 9.1.1
- **Execution date:** 2026-11-03

## 2. Testing Objective

The objective of testing is to evaluate functional behavior, command validation, security-related input handling, media-controller operations, software integration, reliability scenarios, performance, and privacy-related requirements.

This report summarizes the historical and later automated test executions and identifies requirements that remain unverified.

## 3. Test Execution Summary

| Test Execution | Passed | Failed | Errors | Skipped | Duration |
|---|---:|---:|---:|---:|---:|
| Historical additional security/NFR tests | 13 | 0 | 0 | 0 | 0.09 sec |
| Final targeted unit tests | 93 | 0 | 0 | 0 | 0.69 sec |
| Final system-validation tests | 19 | 0 | 0 | 0 | 0.20 sec |

The unit-test execution also reported 20 additional passing subtests. These are reported separately from the 93 pytest test cases.

The executions above were separate runs. Their counts are not presented as one combined test-suite execution.

## 4. Test Environments

**Historical additional security/NFR execution:**
- Operating system: Windows 10
- Python: 3.13.1
- Pytest: 8.3.4

**Later targeted unit and system-validation executions:**
- Operating system: Windows
- Python: 3.11.9
- Pytest: 9.1.1

The results are kept separate because they were collected using different environments and test scopes.

## 5. Testing Areas Covered

| Testing Area | Evidence | Result |
|---|---|---|
| Command-service behavior | Targeted unit tests | Passed |
| Command normalization and validation | Targeted unit tests | Passed |
| Intent processing and variations | Targeted unit tests | Passed |
| Confidence validation | Unit and system-validation tests | Passed |
| Unsupported and ambiguous command rejection | Unit and system-validation tests | Passed |
| Media-controller operations | Targeted unit tests | Passed |
| Controller error handling | Unit and system-validation tests | Passed |
| Software media integration behavior | System-validation tests using simulated VLC interface | Passed |
| Native libVLC product demonstration | Separate Sprint 2 demonstration evidence | Demonstrated |
| Speech-recognition accuracy measurement | No formal measurement available | Not Run |
| Full application startup performance | No measurement available | Not Run |
| End-to-end voice-command latency | No measurement available | Not Run |
| Two-hour continuous-operation reliability | No measurement available | Not Run |
| Complete microphone privacy verification | No verification available | Not Verified |
| Complete application-level access control | No verification available | Not Verified |

## 6. Defect Summary

The recorded automated executions reported zero failures and zero errors.

This statement applies to the test executions documented in this report. It does not establish that the complete application is defect-free.

## 7. Performance Summary

The historical additional security/NFR execution recorded:
- Test-suite execution time: 0.09 seconds.
- Command-service execution time: 0.009 ms.

The later targeted unit and system-validation executions recorded:
- Unit-test execution time: 0.69 seconds.
- System-validation execution time: 0.20 seconds.

These are test execution and service-call measurements. They do not establish full application startup time or microphone-to-response latency.

## 8. Security and Privacy Summary

The automated tests provide evidence for the tested command-validation scenarios, unsupported-intent rejection, confidence validation, controller execution