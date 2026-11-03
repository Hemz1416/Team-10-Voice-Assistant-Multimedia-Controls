# Code Coverage Report

## 1. Project Information

| Field | Value |
|---|---|
| Project | Team 10 – Voice Assistant for Multimedia Controls |
| Report | Code Coverage Report |
| Measurement date | 2026-11-03 |
| Source scope | `src/` |
| Source snapshot | `73e7425` (source archive supplied for this report run) |
| Environment | Linux x86_64, Python 3.13.5, pytest 9.0.2, Coverage.py 7.13.3 |

## 2. Objective and Method

This report records the proportion of executable source statements/lines in `src/` exercised by the complete automated test suite. Coverage was measured with branch measurement enabled so the separate branch-coverage report could also be generated.

**Commands:**

```bash
python -m coverage erase
python -m coverage run --branch --source=src -m pytest -q
python -m coverage report -m
python -m coverage json -o coverage.json
```

## 3. Overall Results

| Metric | Result |
|---|---:|
| Test execution | 105 passed, 11 subtests passed, 0 failures |
| Executable statements/lines measured | 411 |
| Statements/lines executed | 286 |
| Statements/lines not executed | 125 |
| **Statement/line coverage** | **69.6%** |

Statement/line coverage is calculated as 286 executed statements divided by 411 measured statements. The overall Coverage.py combined percentage is lower because it also accounts for branch opportunities; branch coverage is reported separately in `branch_coverage_report.md`.

## 4. Coverage by Source Module

| Source module | Statements | Executed | Not executed | Statement coverage |
|---|---:|---:|---:|---:|
| `src/command_service.py` | 22 | 21 | 1 | 95.5% |
| `src/command_validator.py` | 17 | 17 | 0 | 100.0% |
| `src/event_logger.py` | 6 | 0 | 6 | 0.0% |
| `src/feedback.py` | 4 | 0 | 4 | 0.0% |
| `src/integration_app.py` | 58 | 0 | 58 | 0.0% |
| `src/intent_processor.py` | 28 | 27 | 1 | 96.4%* |
| `src/media_controller.py` | 229 | 202 | 27 | 88.2%* |
| `src/models.py` | 19 | 19 | 0 | 100.0% |
| `src/speech_input.py` | 28 | 0 | 28 | 0.0% |
| **Total** | **411** | **286** | **125** | **69.6%** |

*The per-module percentage in the table is executed statements divided by measured statements. Coverage.py's terminal `Cover` column may show a lower combined figure because it includes branch coverage as well as statements.*

## 5. Interpretation

The command validator and data models were fully covered by this test run. The command service and intent processor had high statement coverage. The media controller had substantial coverage but still contained unexecuted statements.

The modules `speech_input.py`, `integration_app.py`, `feedback.py`, and `event_logger.py` were not executed by the automated suite in this run. Their zero statement coverage does not prove those components are defective; it means this test run did not exercise them. In particular, live speech capture and full application orchestration need dedicated test execution to produce coverage evidence.

## 6. Limitations

- The measurement is tied to source snapshot `73e7425`; re-run it on final `main` if source code changed after that snapshot.
- Coverage measures whether code was executed, not whether every behavior was correct.
- Passing tests and high coverage do not by themselves prove compliance with latency, accuracy, privacy, or long-duration reliability targets.
- A test-double-based integration path does not replace execution with the actual target microphone, VLC installation, and audio devices.

## 7. Conclusion

The complete automated test suite passed, and measured source statement/line coverage was **69.6% (286/411)**. Coverage is incomplete, especially for speech input, application orchestration, feedback, and event logging. These uncovered areas should be considered when interpreting the report and planning any additional validation.
