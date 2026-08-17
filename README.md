# Playwright E2E Test Automation Framework

End-to-end test automation framework built with Playwright and Python, following the Page Object Model pattern, testing the full purchase flow of [SauceDemo](https://www.saucedemo.com) — from login through checkout.

## ✨ Features

- **Page Object Model (POM)** — page logic fully decoupled from test logic
- **Reusable fixtures** — including a pre-authenticated session fixture, avoiding repeated login steps
- **Multiple test scenarios** — happy path, invalid credentials, locked-out users, cart operations, checkout validation
- **HTML reports** — self-contained, shareable test reports generated on every run
- **CI/CD with GitHub Actions** — tests run automatically on every push and pull request
- **Headless & headed modes** — visual debugging locally, headless execution in CI

## 🏗️ Architecture

```
Test → Fixture → Page Object → Playwright Locator
```

- **Page Objects** (`pages/`) — one class per page, encapsulating locators and actions. If the UI changes, only the Page Object needs updating — not every test that touches that page.
- **Fixtures** (`tests/conftest.py`) — reusable setup, including a `logged_in_page` fixture that composes the login flow so tests don't repeat authentication steps.
- **Tests** (`tests/`) — pure assertions against Page Object methods, with no direct selector manipulation.

```
playwright-automation/
├── pages/            # Page Object Model classes
├── tests/            # test suites and fixtures
├── config/           # environment settings and test data
├── reports/          # generated HTML reports (gitignored)
└── .github/workflows/ # CI/CD pipeline
```

## 🛠️ Stack

- **Playwright** — browser automation
- **Pytest** — test runner
- **pytest-playwright** — Playwright/Pytest integration
- **pytest-html** — HTML test reports
- **pytest-xdist** — parallel test execution
- **GitHub Actions** — CI/CD pipeline

## 🚀 Running the tests

### Prerequisites
- Python 3.12+

### Setup

```bash
git clone <repo-url>
cd playwright-automation
python -m venv venv
venv\Scripts\Activate.ps1   # Windows
# source venv/bin/activate  # macOS/Linux

pip install -r requirements.txt
playwright install chromium
```

### Run all tests (headless)

```bash
pytest
```

### Run with visible browser (useful for debugging)

```bash
pytest --headed
```

### Run a specific suite

```bash
pytest tests/test_login.py -v
```

### Run in parallel

```bash
pytest -n auto
```

An HTML report is generated automatically at `reports/report.html` after every run.

## 📖 Test coverage

| Suite | Scenarios |
|---|---|
| Login | successful login, locked-out user, invalid password |
| Inventory | add/remove product, multiple products, sort by price |
| Cart | items persist in cart, remove item from cart page |
| Checkout | full purchase flow, required-field validation |

## 🔐 Design decisions

- **Page Object Model** keeps selectors in one place per page, so UI changes require a single update instead of touching every test file.
- **Text-based locators** (`has_text=...`) are preferred over brittle CSS/XPath chains where possible, since they mirror how a real user identifies elements and are more resilient to markup changes.
- **Composed fixtures** (`logged_in_page`) avoid duplicating setup logic across test files — a common source of flaky, hard-to-maintain test suites.
- **Headless by default, headed on demand** — CI environments run faster in headless mode, while local development benefits from watching the browser interact with the page.

## 🤖 CI/CD

Every push and pull request to `main` triggers the GitHub Actions workflow, which installs dependencies, runs the full suite in headless mode, and uploads the HTML report as a build artifact — accessible from the Actions tab even when tests fail.
