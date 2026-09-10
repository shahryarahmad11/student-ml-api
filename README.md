cat << 'EOF' > README.md
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

### Part 13 — Git Tag and Release Version
- Created Git tag `v1.0.0` pointing to commit `5b87aeb` on `main`.
- Published tag to GitHub via `git push origin v1.0.0`.
- Established 1:1 mapping between Git release tag `v1.0.0` and GHCR image tag `1.0.0`.

### Part 14 — Automated Release Workflow
- Configured `.github/workflows/release.yml` triggered exclusively on semantic version tags matching `v*.*.*`.

### Part 15 — Release Pipeline Requirements
- Implemented step-by-step pipeline execution: Checkout $\rightarrow$ Test execution (`pytest`) $\rightarrow$ Registry authentication (`ghcr.io`) $\rightarrow$ Build and tag $\rightarrow$ Registry push.
- Applied dynamic version extraction (`${GITHUB_REF_NAME#v}`) to map Git tag `v1.0.0` to Docker tag `1.0.0` without hard-coding values.
- Configured multi-tag publishing targeting both `student-ml-api:1.0.0` and `student-ml-api:latest`.

### Part 16 — Registry Verification
- Verified GitHub Container Registry contains container image `student-ml-api` with dual tags: `1.0.0` and `latest`.
- Recorded published image digest: `sha256:d51bdd440a96334e1d6fb6da5deb209b11f861c74dd9fe250c423bfe15dbbc70`.

### Part 17 — Artifact Reproducibility
- Removed local Docker image `student-ml-api:1.0.0` to verify clean execution state.
- Pulled image directly from registry: `docker pull ghcr.io/shahryarahmad11/student-ml-api:1.0.0`.
- Executed downloaded image: `docker run -d --name student-ml-api -p 5000:5000 ghcr.io/shahryarahmad11/student-ml-api:1.0.0`.
- Verified health endpoint via `curl http://localhost:5000/health`, returning: `{"status":"healthy","application":"student-ml-api","version":"1.0.0"}`.
- Confirmed runtime reproducibility from remote container registry without local build dependencies.

### Part 18 — Develop Version 1.1.0
- Created feature branch `feature/model-metadata`.
- Updated `VERSION` file to `1.1.0`.
- Expanded `/health` endpoint in `app.py` to return `application_version: 1.1.0` and `model_version: model-1`.
- Updated pytest suite in `tests/test_app.py` to assert against the version 1.1.0 schema response.

### Part 19 — Release Version 1.1.0 Pipeline Attempt
- Created Git release tag `v1.1.0` pointing to commit `cf4aec9` on `main`.
- Published tag to remote repository via `git push origin v1.1.0` to trigger release automation.

### Part 20 — Rollback Exercise & Advantage Explanation
- Simulated production rollback following a hypothetical issue in version `1.1.0`.
- Executed immediate recovery without modifying application source code or rebuilding image artifacts:
  - Stopped running container: `docker rm -f student-ml-api`
  - Instantly redeployed proven stable image: `docker run -d --name student-ml-api -p 5000:5000 ghcr.io/shahryarahmad11/student-ml-api:1.0.0`
  - Verified endpoint output via `curl http://localhost:5000/health`, confirming active operational status on version `1.0.0`.

**Why Container Registry Rollback Superiority Over Traditional Deployment (`git clone` $\rightarrow$ `pip install` $\rightarrow$ `python app.py`):**
1. **Zero Build/Compile Overhead:** Fetching pre-built container images bypasses dependency resolution, compilation steps, and remote package downloads (PyPI), cutting recovery time from minutes to seconds.
2. **Deterministic Immutability:** Pre-tested Docker images guarantee identical execution environments across development and production, eliminating unexpected runtime failures caused by transitive dependency updates or missing system libraries.
3. **No Local Runtime Toolchain Dependency:** Host nodes do not require Python interpreters, virtual environment configurations, or build tools—only a lightweight container runtime (`docker`/`containerd`).

### Part 21 — Traceability & Automated Release Workflow Failure Analysis

#### Recorded Repository Lineage (v1.1.0):
- **Pull Request:** `#6`
- **Merge Commit SHA:** `cf4aec9`
- **Git Tag:** `v1.1.0`
- **Target Container Tag:** `student-ml-api:1.1.0`

#### Automated Release Pipeline Troubleshooting & Technical Post-Mortem:
Multiple release workflow execution attempts for tag `v1.1.0` failed in GitHub Actions during the automated build stage (`release.yml`). 

**Root Cause Analysis:**
1. **Runner Environment Mismatch:** Local tests were validated in WSL on Python `3.14`, while GitHub Actions utilized `ubuntu-latest` with Python `3.11`.
2. **Dependency Resolution in CI Runner:** During the release workflow execution, `pytest` encountered module loading errors due to implicit dependencies missing from the ephemeral GitHub Actions virtual runner context.
3. **Branch Protection Interactions:** Attempts to commit workflow dependency fixes directly to `main` were appropriately rejected by GitHub's branch protection policies (`GH006`), requiring iterative Pull Requests that unlinked the tag trigger from the target commit.

### Part 22 — Conceptual Separation of CI vs. Release Workflows

In production MLOps architecture, workflows are separated by responsibility:

| Workflow Dimension | Continuous Integration (`ci.yml`) | Automated Release (`release.yml`) |
| :--- | :--- | :--- |
| **Trigger Mechanism** | Pull Requests targeting `main` and pushes to feature branches | Semantic version tags matching `v*.*.*` pushed to `main` |
| **Core Responsibilities** | Code linting, unit testing (`pytest`), and Docker build validation | Full testing, dynamic versioning, image tagging, and publishing |
| **Registry Publishing** | **DISABLED** (Never publishes build artifacts) | **ENABLED** (Publishes tagged images to GHCR) |

#### MLOps Engineering Rationale: Why Publishing Container Images on Every PR is Undesirable

1. **Registry Pollution & Storage Bloat:** Generating and publishing Docker images for every pull request commit fills the container registry with unverified, short-lived artifacts, driving up storage costs and registry clutter.
2. **Security & Supply Chain Vulnerabilities:** Unmerged PR code may contain untested third-party packages, security vulnerabilities, or malicious code. Publishing untrusted images to a public/shared registry introduces supply chain risks.
3. **Race Conditions & Tag Overwrites:** Multiple open PRs attempting to tag images as `latest` or `dev` leads to non-deterministic registry tags where untested feature code overwrites stable development targets.
4. **Strict Release Gate Enforcement:** Releasing an artifact must signify that code has cleared code review, automated testing, security scanning, and PR approval. Separating CI validation from Release publishing guarantees that only vetted, tagged code lands in production registries.

### Part 23 — Advanced Challenge: OCI Image Metadata
- Configured OCI (Open Container Initiative) standard labels during Docker builds in `.github/workflows/release.yml` and `Dockerfile`.
- Injected build parameters to establish full artifact traceability:
  - **Application Version:** `1.1.0` (`org.opencontainers.image.version`)
  - **Git Commit Revision:** `0fd894e` (`org.opencontainers.image.revision`)
  - **Repository Source:** `https://github.com/shahryarahmad11/student-ml-api` (`org.opencontainers.image.source`)
  - **Build Timestamp:** `2026-09-10T18:15:23Z` (`org.opencontainers.image.created`)
- Built local image with build arguments:
  ```bash
  docker build \
    --build-arg VERSION=1.1.0 \
    --build-arg COMMIT_SHA=$(git rev-parse --short HEAD) \
    --build-arg BUILD_DATE=$(date -u +'%Y-%m-%dT%H:%M:%SZ') \
    -t student-ml-api:1.1.0-metadata .
### Part 24 — Advanced Challenge: Commit SHA Tagging Execution & Rationale
- Configured and executed multi-tag build mapping the short Git commit SHA (`c5e1865`) directly to the container registry image.
- Added `--default-timeout=100` to `pip install` inside `Dockerfile` to handle transient PyPI network delays.
- Executed local multi-tag commands:
  ```bash
  docker build \
    --build-arg VERSION=1.1.0 \
    --build-arg COMMIT_SHA=$(git rev-parse --short HEAD) \
    --build-arg BUILD_DATE=$(date -u +'%Y-%m-%dT%H:%M:%SZ') \
    -t ghcr.io/shahryarahmad11/student-ml-api:$(git rev-parse --short HEAD) .
    
  docker tag ghcr.io/shahryarahmad11/student-ml-api:c5e1865 ghcr.io/shahryarahmad11/student-ml-api:1.1.0
  docker tag ghcr.io/shahryarahmad11/student-ml-api:c5e1865 ghcr.io/shahryarahmad11/student-ml-api:latest
REPOSITORY                                 TAG        IMAGE ID       CREATED          SIZE
ghcr.io/shahryarahmad11/student-ml-api    1.1.0      554b0efe7fb5   10 minutes ago   168MB
ghcr.io/shahryarahmad11/student-ml-api    c5e1865    554b0efe7fb5   10 minutes ago   168MB
ghcr.io/shahryarahmad11/student-ml-api    latest     554b0efe7fb5   10 minutes ago   168MB
### Part 25 — Advanced Challenge: Docker Build Cache Analysis

#### Build Output Comparison & Layer Reuse Observation:
1. **Modifying `app.py` only:**
   - **Reused Layers:** `WORKDIR /app`, `COPY requirements.txt .`, and `RUN pip install --no-cache-dir --default-timeout=100 -r requirements.txt` returned `CACHED`.
   - **Re-executed Layers:** Only `COPY . .` and final image export executed.
2. **Modifying `requirements.txt` only:**
   - **Invalidated Layers:** Modifying `requirements.txt` invalidated the cache at `COPY requirements.txt .`.
   - **Re-executed Layers:** Docker was forced to re-run the expensive `RUN pip install` step and every subsequent layer from scratch.

#### Architectural Rationale: Layer Ordering Best Practices
Ordering Docker instructions as:
dockerfile
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app.py .

---

### Part 26 — MLOps Failure Analysis & Diagnostic Log

#### Failure Case 1: Dependency Installation Read Timeout (`pip install`)
- **Symptom:** Docker build failed during package installation (`RUN pip install --no-cache-dir -r requirements.txt`) with `pip._vendor.urllib3.exceptions.ReadTimeoutError: HTTPSConnectionPool(host='files.pythonhosted.org', port=443): Read timed out.` and `exit code: 2`.
- **Root Cause:** Transient network latency and socket timeouts while downloading large wheels (`pydantic-core`, `pytest`) from PyPI inside the ephemeral container build context.
- **Evidence:** Terminal output log showing `TimeoutError: The read operation timed out` during package download at `41.0/337.4 kB`.
- **Correction:** Updated `Dockerfile` to configure an explicit extended socket timeout flag: `RUN pip install --no-cache-dir --default-timeout=100 -r requirements.txt`.

#### Failure Case 2: Protected Branch Direct Push Rejection (`main`)
- **Symptom:** Terminal command `git push origin main` was rejected with `remote: error: GH006: Protected branch update failed for refs/heads/main.`
- **Root Cause:** GitHub Repository Branch Protection rules enforced on `main` blocked direct commit pushes to mandate that all code modifications arrive via approved Pull Requests with passing `ci-checks`.
- **Evidence:** Git error output stating `! [remote rejected] main -> main (protected branch hook declined) error: failed to push some refs`.
- **Correction:** Created a dedicated feature branch (`git checkout -b <branch-name>`), pushed changes, opened a Pull Request targeting `main`, verified automated status checks passed, and completed the merge via **Squash and merge**.

#### Failure Case 3: Missing Remote Release Image Tag (`404 Not Found`)
- **Symptom:** Running `docker pull ghcr.io/shahryarahmad11/student-ml-api:1.1.0` failed with `Error response from daemon: failed to resolve reference "ghcr.io/shahryarahmad11/student-ml-api:1.1.0": ghcr.io/shahryarahmad11/student-ml-api:1.1.0: not found`.
- **Root Cause:** The Git tag `v1.1.0` was attached locally to an older commit that was already pushed, causing subsequent `git push origin v1.1.0` commands to report `Everything up-to-date` without triggering the tag-based release workflow (`release.yml`).
- **Evidence:** Terminal output showing `Everything up-to-date` on tag push while GHCR contained no published `1.1.0` artifact.
- **Correction:** Force-deleted the stagnant local and remote tags (`git tag -d v1.1.0 && git push origin :refs/tags/v1.1.0`), re-tagged the latest commit on `main`, and pushed to trigger the automated release pipeline.
```
