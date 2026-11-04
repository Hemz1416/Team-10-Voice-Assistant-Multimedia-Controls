# CI/CD Pipeline & Quality Assurance

This document details the Continuous Integration and Continuous Delivery (CI/CD) architecture implemented for the **Team-10 Voice Assistant Multimedia Controls** project using GitHub Actions.

---

## 1. Executive Quality & Metrics Dashboard

| Quality Gate | Metric / Tool | Standard / Threshold | Achieved Score | Status |
| :--- | :--- | :---: | :---: | :---: |
| **Code Linting** | Ruff (`pyproject.toml`) | 0 Violations (PEP 8 / Bugbear) | **10.00 / 10.00 (100% Clean)** | 🟢 **PASS** |
| **Unit & Integration Tests** | `pytest` | 100% Pass Rate | **137 / 137 Passed (0.83s)** | 🟢 **PASS** |
| **Code Coverage** | `pytest-cov` | **>= 80.0%** | **92.96% (383/412 lines)** | 🟢 **PASS** |
| **Coverage Artifacts** | XML & HTML Reports | Stored in GitHub Actions | `coverage.xml`, `htmlcov/` | 📦 **RETAINED** |
| **Delivery Packaging (CD)** | `git archive` | Deterministic release bundle | `voice-assistant-<sha>.zip` | 📦 **RETAINED** |

---

## 2. CI/CD Architecture in Our Project

- **Continuous Integration (CI):** Every push or pull request targeting `main` executes on a clean `ubuntu-latest` runner. The pipeline executes static analysis (Ruff), tallies a **10.0-scale Linting Quality Score**, runs **137 automated unit and integration tests**, and verifies **>= 80% statement coverage** across all application modules.
- **Continuous Delivery (CD):** Once all CI quality gates pass on `main`, the packaging job automatically bundles the production source tree into a clean, reproducible ZIP distribution archive ready for deployment.

---

## 3. Workflow Triggers & Execution Scoping

The pipeline is defined in [`.github/workflows/tests.yml`](../.github/workflows/tests.yml).

Triggers are strictly scoped to the `main` branch to eliminate redundant duplicate runs:

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

## 4. Automated Code Linting & Quality Score (Ruff)

- **Engine:** [Ruff](https://docs.astral.sh/ruff/) (`ruff>=0.1.0`), configured in [`pyproject.toml`](../pyproject.toml).
- **Rule Selection:** `E`, `W` (pycodestyle), `F` (pyflakes), `I` (isort), `UP` (pyupgrade), `B` (bugbear), `RUF` (ruff checks).
- **Automated Quality Scorer (`scripts/lint_score.py`):**
  - Evaluates repository violations across all Python source and test files.
  - Computes an automated score out of 10.0:
    $$\text{Quality Score} = \max\left(0.0, 10.0 - (\text{violations} \times 0.2)\right)$$
  - Current Score: **10.00 / 10.00 (Grade: A+ PERFECT | 0 violations | 100% cleanliness)**.
  - Generates an executive summary card directly in the GitHub Actions **Job Summary**.

---

## 5. Automated Unit & Integration Testing (pytest)

- **Test Suite Scope:** Located under [`tests/`](../tests/):
  - **Unit Tests:** Command validation (`test_command_validator.py`), intent processing (`test_intent_processor.py`), service routing (`test_command_service.py`), logging (`test_event_logger.py`), feedback (`test_feedback.py`).
  - **Hardware Mocking:** Offline speech recognition (`test_speech_input.py`), continuous integration app loop (`test_integration_app.py`).
  - **Functional Multimedia:** Play, pause, resume, stop, next/previous wrap-around, volume stepping, volume clamping, mute toggling (`test_functional_commands.py`, `test_media_controller.py`).
  - **Security NFRs:** Exception shielding (`test_security_nfr.py`, `test_additional_security_nfr.py`), malicious input rejection, bounds checking.
  - **Integration Pipeline:** Multi-stage intent to controller execution (`test_media_integration.py`).
- **Local Test Output:** **137 passed, 20 subtests passed (0.83s)**.

---

## 6. Automated Code Coverage

- **Engine:** `pytest-cov>=4.0.0` measuring all files under `src/`.
- **Enforcement Command:**
  ```bash
  python -m pytest -v \
    --cov=src \
    --cov-report=term-missing \
    --cov-report=xml:coverage.xml \
    --cov-report=html:htmlcov
  ```
- **Module-by-Module Coverage Breakdown:**

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
| `src/media_controller.py` | 230 | 25 | **89%** |
| **TOTAL PROJECT** | **412** | **29** | **92.96%** |

---

## 7. Artifact Retention & Verification

Generated reports are automatically preserved in GitHub Actions:
- **`python-coverage-report`** (30-day retention):
  - `coverage.xml`: Cobertura XML report for automated tools.
  - `htmlcov/`: Full interactive HTML report with line-by-line colored source coverage.
- **`voice-assistant-package`** (30-day retention):
  - Produced by the CD `package` job on `main` push: `dist/voice-assistant-<sha>.zip`.

---

## 8. Presentation Walkthrough for Evaluators

1. In GitHub, navigate to **Actions** ➔ Open latest run of **CI/CD Pipeline**.
2. **Show the Job Summary Card:** The rendered Markdown table highlights the **10.0/10.0 Lint Score** and **92.96% Coverage Score**.
3. **Show the Console Logs:**
   - In `lint`, expand `Run Ruff linter and compute Quality Score` (shows 10.00/10.00).
   - In `test`, expand `Run tests with coverage` (shows 137 passed and 92.96% coverage table).
4. **Show Artifacts:** Scroll down to the bottom of the Summary page to show and download `python-coverage-report` and `voice-assistant-package`.
