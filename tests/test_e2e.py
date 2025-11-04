import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()

def test_swagger_ui(browser):
    page = browser.new_page()
    page.goto("http://127.0.0.1:8000/docs")
    assert "Swagger UI" in page.title()
