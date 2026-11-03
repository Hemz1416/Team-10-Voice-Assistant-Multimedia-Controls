# Branch Coverage Report

## 1. Project Information

| Field | Value |
|---|---|
| Project | Team 10 – Voice Assistant for Multimedia Controls |
| Report | Branch Coverage Report |
| Measurement date | 2026-11-03 |
| Source scope | `src/` |
| Source snapshot | `73e7425` (source archive supplied for this report run) |
| Environment | Linux x86_64, Python 3.13.5, pytest 9.0.2, Coverage.py 7.13.3 |

## 2. Objective and Method

Branch coverage measures whether the possible destinations of conditional control-flow decisions in the source code were exercised by the test suite. The measurement was generated together with statement coverage.

**Execution commands:**

```bash
python -m coverage erase
python -m coverage run --branch --source=src -m pytest -q
python -m coverage json -o coverage.json
```

## 3. Overall Results

| Metric | Result |
|---|---:|
| Total branch destinations measured | 142 |
| Branch destinations executed | 97 |
| Branch destinations not executed | 45 |
| Partially covered branches reported by Coverage.py | 19 |
| **Branch coverage** | **68.3%** |

Branch coverage is calculated as 97 executed branch destinations divided by 142 measured branch destinations.

## 4. Branch Coverage by Source Module

| Source module | Branches measured | Branches covered | Branches not covered | Branch coverage |
|---|---:|---:|---:|---:|
| `src/command_service.py` | 8 | 7 | 1 | 87.5% |
| `src/command_validator.py` | 12 | 12 | 0 | 100.0% |
| `src/feedback.py` | 2 | 0 | 2 | 0.0% |
| `src/integration_app.py` | 12 | 0 | 12 | 0.0% |
| `src/intent_processor.py` | 14 | 13 | 1 | 92.9% |
| `src/media_controller.py` | 90 | 65 | 25 | 72.2% |
| `src/speech_input.py` | 4 | 0 | 4 | 0.0% |
| **Total** | **142** | **97** | **45** | **68.3%** |

`src/__init__.py`, `src/event_logger.py`, and `src/models.py` contain no measured branch destinations in this run, so a branch percentage is not applicable to those modules.

## 5. Interpretation

All measured branches in `command_validator.py` were exercised. The intent processor and command service also achieved high branch coverage. Remaining uncovered branch destinations are concentrated in the media controller and the application orchestration, feedback, and speech-input paths.

The zero branch coverage in `integration_app.py`, `speech_input.py`, and `feedback.py` indicates that the current automated suite did not exercise those conditional paths. Additional tests using the full application entry point and suitable audio/input test doubles would be needed to measure those paths.

## 6. Limitations

- This report applies to source snapshot `73e7425`; regenerate coverage on the final repository `main` branch if source files changed after that snapshot.
- Branch coverage is a test-execution metric. It does not establish that requirements are satisfied or that all output combinations are correct.
- The automated integration tests use fake VLC components; no branch-coverage claim is made for a live microphone, physical audio device, or real VLC session beyond what the source-level tests exercised.

## 7. Conclusion

Measured branch coverage was **68.3% (97/142 branch destinations)**. The test suite exercised all branches in command validation, with remaining gaps concentrated in media-controller decisions and modules not exercised by the current automated run. The measured result is recorded as evidence; no minimum branch-coverage target was specified in the available evaluation checklist or FAQ.
