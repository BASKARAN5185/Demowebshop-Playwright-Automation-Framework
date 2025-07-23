---

# 🧪 Demowebshop Test Automation Framework

This repository contains a scalable, maintainable test automation framework built using **Playwright for Python**. It is designed using the **Page Object Model (POM)** design pattern and automates key functional flows of the [Demowebshop](https://demowebshop.tricentis.com/) application.

---

## 📌 Key Features

* ✅ **Playwright with Python** for fast, reliable browser automation
* ✅ **Pytest** for structured, readable test execution
* ✅ **Page Object Model (POM)** for clean separation of concerns
* ✅ **Cross-browser Testing** support (Chromium, Firefox, WebKit)
* ✅ **Allure Reporting** integration *(optional)*
* ✅ Easy-to-maintain, extensible test structure

---

## 🧱 Technology Stack

| Component           | Description               |
| ------------------- | ------------------------- |
| **Language**        | Python 3.8+               |
| **Automation Tool** | Playwright (Python)       |
| **Test Runner**     | Pytest                    |
| **Design Pattern**  | Page Object Model (POM)   |
| **Reporting**       | Allure Reports (Optional) |

---

## 📁 Project Structure

```
demowebshop-playwright/
│
├── pages/                    # Page Object classes
│   ├── base_page.py
│   ├── home_page.py
│   ├── login_page.py
│   ├── register_page.py
│   └── ...
│
├── tests/                    # Test suites
│   ├── test_login.py
│   ├── test_registration.py
│   └── ...
│
├── utils/                    # Configuration, test data, helpers
│   ├── config.py
│   └── test_data.py
│
├── conftest.py              # Global Pytest fixtures
├── pytest.ini               # Pytest configuration
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-org/demowebshop-playwright.git
cd demowebshop-playwright
```

### 2. Set Up Virtual Environment

```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Playwright Browsers

```bash
playwright install
```

---

## ✅ Running Tests

### Run all tests:

```bash
pytest
```

### Run a specific test file:

```bash
pytest tests/test_login.py
```

### Run tests with verbose output:

```bash
pytest -v
```

---

## 📊 Generate Allure Report (Optional)

1. Install Allure:

```bash
brew install allure  # macOS
# or download from https://docs.qameta.io/allure/
```

2. Run tests and generate report:

```bash
pytest --alluredir=reports/
allure serve reports/
```

---

## 📄 Sample Test Case

```python
def test_valid_login(page):
    home = HomePage(page)
    login = LoginPage(page)

    home.goto_homepage()
    home.click_login()
    login.login("user@example.com", "securePassword123")

    assert home.is_user_logged_in()
```

---

## 🧱 Sample Page Object

**pages/login\_page.py**

```python
class LoginPage:

    def __init__(self, page):
        self.page = page
        self.email_input = page.locator("#Email")
        self.password_input = page.locator("#Password")
        self.login_button = page.locator("input[value='Log in']")

    def login(self, email, password):
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.login_button.click()
```

---

## 🛠️ Configuration

You can manage environment-specific variables such as base URLs, credentials, and browser options inside the `utils/config.py` file.

---

## 📦 requirements.txt

```txt
playwright
pytest
pytest-playwright
allure-pytest
```

Install with:

```bash
pip install -r requirements.txt
```

---

## 🧪 Best Practices Followed

* Separation of test logic and page interactions (POM)
* Reusable fixtures and helper functions
* Organized directory structure
* Scalable test case design
* Optional reporting & CI/CD readiness

---

## 🔄 CI/CD Integration

This project can be easily integrated into any CI pipeline (e.g., GitHub Actions, GitLab CI, Jenkins). Add a workflow file that includes:

```yaml
- name: Run Playwright Tests
  run: pytest
```

---

## 👤 Maintainer

**Your Name**
📧 [MailID](mailto:baskarbala5185@gmail.com)
🔗 [GitHub](https://github.com/BASKARAN5185)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---