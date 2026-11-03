# Unit Test Report

## 1. Project Information

| Field | Value |
|---|---|
| Project | Team 10 – Voice Assistant for Multimedia Controls |
| Report | Unit Test Report |
| Test cycle | Sprint 2 / Final evaluation |
| Execution date | 2026-11-03 |
| Execution environment | Windows, Python 3.11.9, pytest 9.1.1 |

## 2. Objective

The objective of unit testing is to verify individual application components, including intent processing, command validation, command-service behavior, media-controller logic, and security-related input handling.

## 3. Scope and Test Execution

The following test files were executed:

| Test file | Test cases passed |
|---|---:|
| `tests/test_command_service.py` | 4 |
| `tests/test_command_validator.py` | 12 |
| `tests/test_intent_processor.py` | 6 |
| `tests/test_intent_variations.py` | 16 |
| `tests/test_media_controller.py` | 39 |
| `tests/test_security_nfr.py` | 16 |
| **Total pytest test cases** | **93** |

**Execution command:**

```cmd
python -m pytest tests/test_command_service.py tests/test_command_validator.py tests/test_intent_processor.py tests/test_intent_variations.py tests/test_media_controller.py tests/test_security_nfr.py -v
```

## 4. Results

| Result | Count |
|---|---:|
| Pytest test cases passed | 93 |
| Additional subtests passed | 20 |
| Failed | 0 |
| Errors | 0 |
| Skipped | 0 |
| Execution time | 0.69 seconds |

**Outcome: PASS for the unit-test scope executed.**

## 5. Areas Verified

- Supported and unsupported intent interpretation.
- Command normalization and validation.
- Confidence-value validation, including invalid and low-confidence values.
- Prevention of rejected commands reaching the media controller.
- Media-controller operations and error handling.
- Security-focused command-service validation and controlled error responses.
- Natural-language command variations and ambiguous input handling.

## 6. Limitations

- This report documents the targeted unit-test execution on Windows using Python 3.11.9 and pytest 9.1.1.
- Unit tests do not, by themselves, verify real microphone capture, complete application startup, physical audio output, or long-duration operation.
- The 20 subtests are reported separately from the 93 collected pytest test cases.

## 7. Conclusion

All 93 pytest cases in the defined unit-test scope passed, along with 20 subtests. No failures, errors, or skips were reported. The execution completed in 0.69 seconds. These results support the tested component behavior and should be considered alongside the system-validation and coverage reports.