# Contributing to fermat‑mcp

Thank you for your interest in contributing to **fermat‑mcp**! This guide explains how to get involved and provides a clear process for code contributions, issue reporting, and community discussion.

---

## Table of Contents

| Section                              | Description                                |
|--------------------------------------|--------------------------------------------|
| [1. Contribution Types](#types)      | What contributions are welcome             |
| [2. Getting Started](#getting‑started) | Forking, setup, and branch workflow        |
| [3. Bug Reports & Features](#bugs‑features) | Issue reporting and feature requests       |
| [4. Pull Request Process](#pull‑requests) | PR workflow and review expectations        |
| [5. Code Style & Testing](#code‑style) | Linting, formatting, CI, tests             |
| [6. Other Ways to Help](#other‑ways)   | Documentation, translations, outreach      |
| [7. Code of Conduct & Licensing](#conduct) | Contributor expectations and license         |
| [8. Acknowledgements](#acknowledgements) | Recognition and thanks                     |

---

## 1. Contribution Types <a name="types"></a>

We welcome contributions in many forms:

- **Code enhancements**: bug fixes, new features, performance improvements  
- **Tests**: new tests, improved coverage, reliability improvements  
- **Documentation**: clarifying README, usage examples, tutorials  
- **Issue triage**: confirming reproducibility, labeling, providing additional context  
- **Community support**: helping others via GitHub discussions or forums  

---

## 2. Getting Started <a name="getting‑started"></a>

Follow this common workflow:

| Step                     | Action                                                                                  |
|--------------------------|-----------------------------------------------------------------------------------------|
| **Fork the repo**        | Click “Fork” on GitHub and clone your copy                                              |
| **Add upstream remote**  | `git remote add upstream https://github.com/abhiphile/fermat-mcp.git`                 |
| **Create a feature branch** | `git checkout -b feature/description` or `fix/issue-123`                             |
| **Install dependencies** | Follow README setup instructions (e.g. via `setup.sh`, Docker)                         |
| **Keep in sync**         | Regularly `git fetch upstream` & `git rebase upstream/main`                            |

---

## 3. Bug Reports & Feature Requests <a name="bugs‑features"></a>

Before submitting an issue, please:

1. Ensure you're using the latest version
2. Search existing issues to avoid duplicates
3. Provide a clear description:
   - Steps to reproduce
   - Expected vs actual behavior
   - Environment details (OS, Python version, etc.)
   - Error logs or minimal reproducible example

For feature requests, describe the problem and proposed solution. Add labels like `bug`, `enhancement`, or `good first issue` as needed.

---

## 4. Pull Request Process <a name="pull‑requests"></a>

| Step               | Guidance                                                                                       |
|--------------------|------------------------------------------------------------------------------------------------|
| **Target branch**  | Submit PRs to `main` branch                                                                     |
| **Link issues**    | Use `Fixes #issue-number` or reference issues in PR description                                 |
| **Keep PR focused**| One feature or fix per PR, with tests or examples                                               |
| **Include context**| Provide sample inputs/outputs or screenshots if applicable                                     |
| **Review process** | Wait for feedback, address requested changes, and ensure CI passes                              |
| **Templates**      | Use PR and issue templates if available                                                         |

Maintain cordial and respectful tone—even when closing or rejecting contributions :contentReference[oaicite:2]{index=2}.

---

## 5. Code Style & Testing <a name="code‑style"></a>

- Follow the style conventions laid out in the project (e.g. Black, RUFF, Flake8)
- Run linting and formatting locally before committing:
  ```bash
  ruff .
  black .
  pytest
