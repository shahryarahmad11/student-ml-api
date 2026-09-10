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

### Part 8 - Merge Strategy Selection & Merge Resolution

#### Selected Strategy: **Squash and Merge**

#### Strategy Justification:
1. **Clean & Linear History on `main`:** Intermediate commits, documentation updates, and failure-testing iterations on `feature/prediction-api` are squashed into a single clean commit on `main`.
2. **Simplified Rollbacks:** Represents the entire inference API delivery (`feat: add prediction endpoint, unit tests, docker, and CI pipeline`) in one commit, making production rollbacks straightforward (`git revert <commit-hash>`).
3. **Traceability:** Links the single squashed commit directly to PR #1 on GitHub for auditability while eliminating commit noise.

#### Handling Branch Protection Merge Blocking & Resolution:
- **Issue Encountered:** Upon attempting to execute the merge, GitHub blocked the action with the error: `Merging is blocked: At least 1 approving review is required by reviewers with write access`. Because GitHub restricts repository owners from approving their own Pull Requests, the rule enabled in Part 7 prevented completion.
- **Resolution Step:** I navigated back to Repository `Settings` -> `Branches` -> `main` Protection Rules and unchecked **Require approvals** while maintaining **Require status checks to pass before merging** (`ci-checks`).
- **Final Merge Execution:** Once the review restriction was updated, the merge gate cleared. I selected **Squash and Merge**, confirmed the pull request merge into `main`, and deleted the feature branch.

### Part 9 - Dockerization & Branch Protection Enforcement Verification

#### Production-Oriented Docker Configuration:
- Implemented a production `Dockerfile` using `python:3.11-slim` (avoiding unpinned `latest` tags).
- Configured efficient image layer caching by placing `requirements.txt` and `pip install --no-cache-dir` prior to copying application source files.
- Defined `WORKDIR /app`, exposed port `5000`, and set `CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "5000"]`.
- Configured `.dockerignore` to exclude `.git`, `.github`, `__pycache__`, `*.pyc`, `.venv`, `.env`, and `tests/` directories.

#### Real-World Branch Protection Enforcement Event:
- **Direct Push Attempt:** Following the setup of Part 7 branch protections, a direct commit push to `main` from terminal failed with `remote: error: GH006: Protected branch update failed for refs/heads/main`.
- **Enforcement Validation:** This error confirmed that the branch protection policies effectively prevent unreviewed or unvalidated local commits from landing directly on production.
- **Resolution via PR Workflow:** To maintain complete compliance without disabling protection, I created a feature branch `docs/part-9-docker-readme`, pushed the changes, submitted Pull Request #2, passed automated `ci-checks`, and squashed and merged into `main`.

### Part 10 - Build and Verify Docker Image Locally
- Configured `VERSION` file with application release `1.0.0`.
- Built local Docker container image using `docker build -t student-ml-api:1.0.0 .`.
- Executed container in background via `docker run -d --name student-ml-api -p 5000:5000 student-ml-api:1.0.0`.
- Verified container endpoint via `curl http://localhost:5000/health`, confirming expected JSON status and version output `1.0.0`.

### Part 11 - Docker Image Inspection

**Extracted Container Details:**
- **Container ID:** `e2b00d4b61dc` (Full: `e2b00d4b61dc55d5920a530f710d9042be98d54ae83fb39ed4c78ca6a5739b78`)
- **Image ID:** `d51bdd440a96` (Full: `sha256:d51bdd440a96334e1d6fb6da5deb209b11f861c74dd9fe250c423bfe15dbbc70`)
- **Exposed Port:** `5000/tcp` (Mapped to host `0.0.0.0:5000`)
- **Running Command:** `uvicorn app:app --host 0.0.0.0 --port 5000`
- **Application Working Directory:** `/app`

**Executed Inspection Commands:**
- `docker images` — Listed all locally cached container images and verified `student-ml-api:1.0.0`.
- `docker ps` — Verified active running state, container name, and host port mapping (`0.0.0.0:5000->5000/tcp`).
- `docker logs student-ml-api` — Inspected live application stdout logs confirming Uvicorn process initialization.
- `docker inspect student-ml-api` — Extracted full JSON metadata for state, network ports, volume mounts, and execution path.
- `docker exec -it student-ml-api sh -c "pwd && exit"` — Verified shell execution and confirmed working directory `/app`.

### Part 12 - Container Registry
- Authenticated with GitHub Container Registry (`ghcr.io`) using a Personal Access Token with `write:packages` scope.
- Tagged local image: `ghcr.io/shahryarahmad11/student-ml-api:1.0.0`.
- Published image to remote registry via `docker push ghcr.io/shahryarahmad11/student-ml-api:1.0.0`.

### Part 13 - Git Tag and Release Version
- Created Git tag `v1.0.0` pointing to commit `5b87aeb` on `main`.
- Published tag to GitHub via `git push origin v1.0.0`.
- Established 1:1 mapping between Git release tag `v1.0.0` and GHCR image tag `1.0.0`.
