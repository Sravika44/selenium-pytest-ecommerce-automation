import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
import pytest
from pages.product import product_page


@pytest.fixture()
def ohrm():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")

    # EdgeDriver is already in PATH
    service = Service(executable_path=r"C:\Users\DELL\OneDrive\Desktop\Webdrivers\msedgedriver.exe")
    driver = webdriver.Edge(service=service, options=options)
    driver.get("https://automationexercise.com")

    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    # Only on test failure
    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("ohrm")
        if driver:
            screenshots_dir = os.path.join(os.getcwd(), "reports", "screenshots")
            os.makedirs(screenshots_dir, exist_ok=True)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot_name = f"{item.name}_{timestamp}.png"
            screenshot_path = os.path.join(screenshots_dir, screenshot_name)

            driver.save_screenshot(screenshot_path)

