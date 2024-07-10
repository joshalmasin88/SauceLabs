import pytest
from selenium import webdriver


# Set option for browser selection
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Pick a browser: ex. chrome, firefox, edge")


@pytest.fixture(scope="class")
def test_setup(request):
    # Check which browser option user selected
    browser = request.config.getoption("--browser")
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    elif browser == 'edge':
        driver = webdriver.Edge()
    request.cls.driver = driver
    yield driver
    driver.close()
    driver.quit()
    print("Test Completed")