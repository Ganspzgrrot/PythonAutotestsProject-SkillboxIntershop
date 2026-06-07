import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    options = Options()
    options.add_argument('--incognito')
    options.page_load_strategy = 'normal'

    service = ChromeService(ChromeDriverManager().install())

    browser = webdriver.Chrome(service=service, options=options)
    browser.implicitly_wait(30)

    yield browser
    browser.quit()