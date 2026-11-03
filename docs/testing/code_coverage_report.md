# Code Coverage Report

## 1. Test Environment

- Operating System: Windows
- Python: 3.11.9
- pytest: 9.1.1
- coverage.py: 7.17.0
- Coverage mode: Statement and branch coverage
- Test command: `python -m coverage run --branch -m pytest tests -v`

## 2. Test Execution Results

- Tests collected: 125
- Tests passed: 125
- Subtests passed: 20
- Failed tests: 0
- Execution time: 1.10 seconds

## 3. Application Source Coverage

Coverage was filtered to the `src/` directory using:

`python -m coverage report --include="src/*" -m`

| Metric | Result |
|---|---:|
| Total statements | 315 |
| Missed statements | 27 |
| Statements covered | 288 |
| Statement coverage | 91% |
| Total branches | 124 |
| Partial branches | 21 |
| Branches covered | 103 |
| Branch coverage | 83% |
| Overall source coverage | 88% |

## 4. Coverage by Source Module

| Module | Coverage |
|---|---:|
| src/__init__.py | 100% |
| src/command_service.py | 93% |
| src/command_validator.py | 100% |
| src/intent_processor.py | 95% |
| src/media_controller.py | 85% |
| src/models.py | 100% |

## 5. Observations

- The application source code achieved 88% overall coverage.
- Statement coverage reached 91%.
- Branch coverage reached 83%.
- The command validator, models, and package initialization achieved 100% coverage.
- The media controller has the largest opportunity for additional coverage improvement.

## 6. Conclusion

The Windows coverage execution completed successfully. All 125 collected tests and 20 subtests passed. The measured application source coverage was 88%, with 91% statement coverage and 83% branch coverage.

These results represent the measured test run and do not imply that every application execution path has been tested.