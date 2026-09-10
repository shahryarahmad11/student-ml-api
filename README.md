# student-ml-api

This repository contains an ML inference API service built with FastAPI as part of an MLOps assignment.

## Prerequisites & Environment Setup

Before running or developing this application, ensure the following environment requirements and tools are installed:
- **Operating System:** Ubuntu / WSL2 (Windows Subsystem for Linux)
- **Python:** Version `3.11` or higher
- **Docker:** Engine and CLI configured and running locally
- **Git:** Configured with user credentials and SSH/HTTPS access to GitHub
- **Package Management:** `pip` upgraded to the latest version
- **System Workarounds & Local Settings:**
  - Resolved system-managed environment restrictions using `--break-system-packages` during local dependency installation.
  - Resolved `pytest` PYTHONPATH module import paths by executing unit tests using `python3 -m pytest`.

---

## Progress & Implementation Log

### Part 1 - Application Setup
- I initialized the repository structure and created the core application files.
- I added `requirements.txt` containing dependencies for FastAPI, Uvicorn, Pytest, and HTTPX.
- I created the `VERSION` file setting the initial application version to `1.0.0`.
- I implemented `app.py` using FastAPI with two endpoints (`GET /health` and `POST /predict`).

### Part 2 - Automated Tests
- I created the unit testing suite in `tests/test_app.py` using `pytest` and FastAPI's `TestClient`.
- I executed and validated all unit tests locally using `python3 -m pytest`.

### Part 3 - Establish a Professional Git Workflow
- I established a feature branch workflow by creating and switching to `feature/prediction-api`.
- I rebased local commits onto `main` to ensure clean history alignment.

### Part 4 - Pull Request Requirements & Docker Containerization
- I created a lightweight production `Dockerfile` based on `python:3.11-slim` exposing port 5000.
- I added `.dockerignore` to exclude local artifacts, tests, and `.git` caches from image builds.
- I opened Pull Request #1 on GitHub targeting `main` and added a professional description covering summary, changes, and testing performed.

### Part 5 - GitHub Actions CI
- I created `.github/workflows/ci.yml` configured to trigger on pull requests targeting `main` and pushes to feature branches.
- I defined a continuous integration job covering code checkout, Python setup, dependency installation, `pytest` unit testing, and Docker build validation.

### Part 6 - Demonstrate Pipeline Failure Gate
- I introduced an intentional test failure in `tests/test_app.py` by changing the health endpoint assertion to an invalid status.
- I verified that GitHub Actions automatically flagged the job as **FAILED**, successfully blocking the PR merge gate.
- I resolved the intentional failure by committing `fix: correct health endpoint test`, pushed to GitHub, and verified the workflow run returned to a **PASSED** (green) status.

### Part 7 - Protect the Main Branch Configuration Log
To safeguard the production branch, prevent accidental direct commits, and mandate continuous integration verification, I enabled **Branch Protection Rules** on the `main` branch via GitHub Repository Settings (`Settings` -> `Branches` -> `Add branch protection rule`).

#### Selected Protection Settings & Rationale:
1. **Branch Pattern:** `main`
2. **Require a pull request before merging:**
   - **Enforced Option:** `Require approvals` (Set to minimum 1 reviewer before merging).
   - **Rationale:** Ensures no direct development or force pushes occur on `main`. All modifications must be submitted via a Pull Request from a feature branch.
3. **Require status checks to pass before merging:**
   - **Enforced Option:** `Require branches to be up to date before merging`.
   - **Target Status Check:** `ci-checks` (GitHub Actions CI Workflow).
   - **Rationale:** Blocks code merging until all unit tests (`pytest`) and image build validations (`docker build`) succeed in GitHub Actions.
4. **Do not allow bypassing the above settings:**
   - **Enforced Option:** Enabled for all users including administrators.
   - **Rationale:** Mandates that strict quality gates apply universally to guarantee total MLOps compliance.
