import pytest, os
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


pytest_plugins = [
   "tests.api.fixtures_api"
]


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome', help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='ru, en', help="Choose language: 'ru' or 'en'")

def browser_chrome_settings(request):
    chrome_service = ChromeService(ChromeDriverManager().install())
    options = Options()
    user_language = request.config.getoption("language")
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    options.add_argument("--disable-gpu")
    options.add_argument("--ignore-certificate-errors")
    headless = os.environ.get('HEADLESS', 'False').lower() == 'true'
    if headless:
        options.add_argument("--headless")
        print("Запущен в headless режиме")
    else:
        print("Запущен в обычном режиме")
    browser = webdriver.Chrome(service = chrome_service, options = options)
    return browser

def browser_firefox_settings(request):
    fp = webdriver.FirefoxProfile()
    user_language = request.config.getoption("language")
    fp.set_preference("intl.accept_languages", user_language)
    browser = webdriver.Firefox(firefox_profile=fp)
    return browser




supported_browsers = {
    'chrome': browser_chrome_settings,
    'firefox': browser_firefox_settings
}

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name in supported_browsers:
        print(f"\nstart {browser_name} browser for test..")
        browser = supported_browsers.get(browser_name)(request)
    else:
        joined_browsers = ', '.join(supported_browsers.keys())
        raise pytest.UsageError(f"--browser_name is invalid, supported browsers: {joined_browsers}")
    yield browser
    print("\nquit browser..")
    browser.quit()