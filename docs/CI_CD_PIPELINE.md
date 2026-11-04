# CI/CD Pipeline & Quality Assurance

This document details the Continuous Integration and Continuous Delivery (CI/CD) architecture implemented for the **Team-10 Voice Assistant Multimedia Controls** project using GitHub Actions.

---

## 1. Executive Quality & Metrics Dashboard

| Quality Gate | Metric / Tool | Standard | Achieved Result | Status |
| :--- | :--- | :---: | :---: | :---: |
| **Code Linting** | Ruff (`pyproject.toml`) | 0 Violations (PEP 8 / Bugbear / Flake8) | **0 Violations (10.00 / 10.00 Clean Score)** | 🟢 **PASS** |
| **Unit & Integration Tests** | `pytest` | 100% Pass Rate | **146 Tests + 20 Subtests (166 Outcomes)** | 🟢 **PASS** |
| **Code Coverage** | `pytest-cov` | High Statement Coverage | **93.48% (387 / 414 statements)** | 🟢 **PASS** |
| **Coverage Artifacts** | XML & HTML Reports | Stored in GitHub Actions | `coverage.xml`, `htmlcov/` | 📦 **RETAINED** |
| **Delivery Packaging (CD)** | `git archive` | Release ZIP bundle | `voice-assistant-<sha>.zip` | 📦 **RETAINED** |

---

## 2. CI/CD Architecture in Our Project

- **Continuous Integration (CI):** Every push or pull request targeting `main` executes on a clean GitHub-hosted `ubuntu-latest` runner. The pipeline executes static analysis (Ruff) verifying **0 violations**, runs **146 automated pytest tests plus 20 subtests (166 total passing execution outcomes)**, and measures runtime statement coverage across all application modules.
- **Continuous Delivery (CD):** Once all CI quality gates pass on `main`, the packaging job automatically bundles the production source tree into a clean, reproducible ZIP distribution archive ready for deployment. Packaging executes only after linting and testing succeed.

---

## 3. Workflow Triggers & Execution Scoping

The pipeline is defined in [`.github/workflows/tests.yml`](../.github/workflows/tests.yml).

Triggers are strictly scoped to the `main` branch:

```yaml
on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]
```

- **Push to `main`:** Executes `lint` and `test` jobs in parallel. Upon passing, triggers the `package` job.
- **Pull Request to `main`:** Executes `lint` and `test` in parallel. Packaging is skipped until merged.

---

## 4. Automated Code Linting (Ruff)

- **Engine:** [Ruff](https://docs.astral.sh/ruff/) (`ruff>=0.1.0`), configured in [`pyproject.toml`](../pyproject.toml).
- **Rule Selection:** `E`, `W` (pycodestyle), `F` (pyflakes), `I` (isort), `UP` (pyupgrade), `B` (bugbear), `RUF` (ruff checks).
- **Primary Evidence:** **0 violations detected across all project modules in `src/`, `tests/`, and `scripts/`**.
- **Project Quality Score (`scripts/lint_score.py`):**
  - Evaluates repository violations across all Python source and test files.
  - Computes a normalized quality score out of 10.0:
    $$\text{Quality Score} = \max\left(0.0, 10.0 - (\text{violations} \times 0.2)\right)$$
  - Current Score: **10.00 / 10.00 (Grade: A+ PERFECT | 0 violations | 100% cleanliness)**.
  - Generates an executive summary card directly in the GitHub Actions **Job Summary**.

---

## 5. Automated Unit & Integration Testing (pytest)

- **Test Suite Scope:** Located under [`tests/`](../tests/):
  - **Unit Tests:** Command validation (`test_command_validator.py`), intent processing (`test_intent_processor.py`, `test_intent_variations.py`), service routing (`test_command_service.py`), logging (`test_event_logger.py`), feedback (`test_feedback.py`).
  - **Hardware Mocking:** Offline speech recognition (`test_speech_input.py`), continuous integration app loop (`test_integration_app.py`).
  - **Functional Multimedia:** Play, pause, resume, stop, next/previous wrap-around, volume stepping, volume clamping, mute toggling, and real-time playback state query (`test_functional_commands.py`, `test_media_controller.py`).
  - **Security NFRs:** Exception shielding (`test_security_nfr.py`, `test_additional_security_nfr.py`), malicious input rejection, bounds checking.
  - **Integration Pipeline:** Multi-stage intent to controller execution (`test_media_integration.py`).
- **Verified Execution Metrics:**
  - **146 Pytest Tests Passed**
  - **20 Additional Subtests Passed**
  - **166 Total Passing Outcomes** (counted by JUnit XML test runner)
  - **Execution Time:** ~0.26s – 0.83s.

---

## 6. Automated Code Coverage

- **Engine:** `pytest-cov>=4.0.0` measuring all files under `src/`.
- **Execution Command:**
  ```bash
  python -m pytest -v \
    --junitxml=test-results.xml \
    --cov=src \
    --cov-report=term-missing \
    --cov-report=xml:coverage.xml \
    --cov-report=html:htmlcov
  ```
- **Module-by-Module Coverage Breakdown (Verified in Actions):**

| Module | Statements | Missed | Coverage % |
| :--- | :---: | :---: | :---: |
| `src/__init__.py` | 0 | 0 | **100%** |
| `src/models.py` | 19 | 0 | **100%** |
| `src/command_validator.py` | 17 | 0 | **100%** |
| `src/event_logger.py` | 6 | 0 | **100%** |
| `src/feedback.py` | 4 | 0 | **100%** |
| `src/integration_app.py` | 58 | 1 | **98%** |
| `src/intent_processor.py` | 28 | 1 | **96%** |
| `src/command_service.py` | 22 | 1 | **95%** |
| `src/speech_input.py` | 28 | 2 | **93%** |
| `src/media_controller.py` | 232 | 22 | **91%** |
| **TOTAL PROJECT** | **414** | **27** | **93.48%** |

### Verified Runtime Code Coverage
The test suite instruments both business logic and I/O integration modules using hardware mocks:
1. `src/speech_input.py` (93%): Mock audio stream & KaldiRecognizer validation (`test_speech_input.py`).
2. `src/integration_app.py` (98%): Continuous CLI integration loops with KeyboardInterrupt and error handlers (`test_integration_app.py`).
3. `src/media_controller.py` (91%): VLC playback controls, volume stepping, mute toggling, and real-time playback state inspection (`test_media_controller.py`).
4. `src/intent_processor.py` (96%): Natural speech intent parsing and synonym expansion (`test_intent_processor.py`, `test_intent_variations.py`).
5. `src/event_logger.py` (100%): Structured timestamped logging verification (`test_event_logger.py`).
6. `src/feedback.py` (100%): Terminal feedback status formatting (`test_feedback.py`).

---

## 7. Artifact Retention & Verification

Generated reports are automatically preserved in GitHub Actions:
- **`python-coverage-report`** (30-day retention):
  - `coverage.xml`: Cobertura XML report for automated tools.
  - `htmlcov/`: Full interactive HTML report with line-by-line colored source coverage.
- **`voice-assistant-package`** (30-day retention):
  - Produced by the CD `package` job on `main` push: `dist/voice-assistant-<sha>.zip`.

---

## 8. Presentation Walkthrough for Evaluators / TA

Follow this exact walkthrough during the demo:

1. **Open the GitHub Actions Run:** Open the latest successful run on `main`.
2. **Show the Three Successful Jobs:** Point out that all three jobs (`Code Linting & Quality Score`, `Tests and Coverage`, `Package application (CD)`) execute remotely on GitHub-hosted Ubuntu runners and are green.
3. **Open `Code Linting & Quality Score`:** Show the Ruff static analysis step verifying **0 violations**.
4. **Open `Tests and Coverage`:** Show the pytest execution logs:
   - **146 passed tests + 20 subtests (166 total outcomes)**.
   - The **93.48% statement coverage table** (387 / 414 statements).
5. **Return to the Summary Page:** Scroll down to the **Artifacts** section and show both uploaded packages:
   - `python-coverage-report`
   - `voice-assistant-package`
6. **Explain the CD Gating:** Point out that the `package` job depends on both `lint` and `test` (`needs: [lint, test]`), ensuring release packages are only generated when all quality checks pass.
