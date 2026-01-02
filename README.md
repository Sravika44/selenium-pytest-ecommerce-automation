# Selenium Pytest Automation Framework

## 📌 Project Overview
This project is an end-to-end automation framework built using **Python, Selenium, and Pytest** to automate key user flows of an e-commerce application.

The framework follows **Page Object Model (POM)** design and supports **HTML reporting, screenshots on failure, and CI execution via Jenkins**.

## 🛠 Tech Stack
- Python
- Selenium WebDriver
- Pytest
- Pytest-HTML
- Jenkins (CI)
- Git & GitHub

## 📂 Framework Structure
project/
├── pages/ # Page Object classes
├── tests/ # Test cases
├── reports/ # HTML reports & screenshots
├── conftest.py # Fixtures & hooks
├── pytest.ini # Pytest configuration
├── requirements.txt
├── README.md

## ✅ Automated Test Scenarios
- User Login
- Product Navigation
- Add Product to Cart
- View Cart Validation
- Product Search
- End-to-End User Flow

## 📸 Screenshots on Failure
Screenshots are automatically captured and saved under:
reports/screenshots/
whenever a test fails.

## 📊 Test Reports
HTML execution reports are generated using **pytest-html**:
reports/report.html
## 📊 Sample Report
> Reports are generated during execution and available in Jenkins builds.
## 🏷 Pytest Markers
The framework supports custom pytest markers to control test execution:

`@pytest.mark.smoke` – Critical smoke tests
### Run examples:
```bash I used mark.smoke in this project 
pytest -m smoke

## ▶️ How to Run Tests Locally
```bash
pip install -r requirements.txt
pytest -v
🔁 CI/CD Integration
This project is integrated with Jenkins to run automated tests on every code push.

👤 Author
Sravika Talari
Automation Test Engineer