# student-ml-api

This repository contains an ML inference API service built with FastAPI as part of an MLOps assignment.

## Progress & Implementation Log

### Part 1 - Application Setup
- I initialized the repository structure and created the core application files.
- I added `requirements.txt` containing dependencies for FastAPI, Uvicorn, Pytest, and HTTPX.
- I created the `VERSION` file setting the initial application version to `1.0.0`.
- I implemented `app.py` using FastAPI with two endpoints (`GET /health` and `POST /predict`).

### Part 2 - Automated Tests
- I created the unit testing suite in `tests/test_app.py` using `pytest` and FastAPI's `TestClient`.
- I resolved module resolution issues using `python3 -m pytest` to run tests locally.

### Part 3 - Establish a Professional Git Workflow
- I established a feature branch workflow by creating and switching to `feature/prediction-api`.
- I rebased local branches onto `main` to ensure clean commit history alignment.

### Part 4 - Pull Request Requirements
- I opened Pull Request #1 on GitHub targeting `main`.
- I updated the PR with a clean description covering summary, changes, and testing performed.

### Part 5 - GitHub Actions CI
- I created `.github/workflows/ci.yml` configured to trigger on pull requests targeting `main` and pushes to feature branches.
- I defined a continuous integration job containing checkout, Python setup, dependency installation, `pytest` unit test execution, and local Docker image build validation.
