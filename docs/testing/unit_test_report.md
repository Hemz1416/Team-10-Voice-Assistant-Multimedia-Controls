# Unit Test Report

## 1. Project Information

| Field | Value |
|---|---|
| Project | Team 10 – Voice Assistant for Multimedia Controls |
| Report | Unit Test Report |
| Test cycle | Sprint 2 / Final evaluation preparation |
| Execution date | 2026-11-03 |
| Source snapshot | `73e7425` (source archive supplied for this report run) |
| Execution environment | Linux x86_64, Python 3.13.5, pytest 9.0.2 |

## 2. Objective

The objective of unit testing is to verify individual application components, including intent processing, command validation, command-service behavior, media-controller logic, and security-related input handling.

## 3. Scope and Test Execution

The unit-test run included the following files:

| Test file | Test cases passed |
|---|---:|
| `tests/test_command_service.py` | 4 |
| `tests/test_command_validator.py` | 10 |
| `tests/test_intent_processor.py` | 5 |
| `tests/test_intent_variations.py` | 12 |
| `tests/test_media_controller.py` | 39 |
| `tests/test_security_nfr.py` | 16 |
| **Total pytest test cases** | **86** |

**Execution command:**

```bash
python -m pytest tests/test_command_service.py tests/test_command_validator.py tests/test_intent_processor.py tests/test_intent_variations.py tests/test_media_controller.py tests/test_security_nfr.py -q
```

## 4. Results

| Result | Count |
|---|---:|
| Pytest test cases passed | 86 |
| Additional unittest subtests passed | 11 |
| Failed | 0 |
| Errors | 0 |
| Skipped | 0 |
| Reported execution time | 0.13 seconds |

<text>**Outcome: PASS for the unit-test scope executed.**</text>

The complete test suite was also executed separately and reported **105 passed, 11 subtests passed, and no failures** in 0.18 seconds.

## 5. Areas Verified

- Supported and unsupported intent interpretation.
- Command normalization and validation.
- Confidence-value validation, including invalid and low-confidence values.
- Prevention of rejected commands reaching the media controller.
- Media-controller operations and error handling using test doubles/mocked dependencies where applicable.
- Security-focused command-service validation and controlled error responses.

## 6. Limitations

- This report run used the supplied source snapshot identified as `73e7425`. Re-run the commands on the final repository `main` branch if application source code has changed since that snapshot.
- The report-generation environment was Linux with Python 3.13.5 and pytest 9.0.2. It is not a replacement for a Windows run using the project's target VLC/audio environment.
- Unit tests do not, by themselves, verify real microphone capture, complete application startup, physical audio output, or long-duration operation.
- The 11 subtests are reported separately from the 86 pytest test cases to avoid double-counting them as ordinary pytest items.

## 7. Conclusion

All 86 pytest cases in the defined unit-test scope passed, along with 11 subtests. No failures, errors, or skips were reported. The result supports the tested component behavior but should be considered together with the separate system-validation and coverage reports.
