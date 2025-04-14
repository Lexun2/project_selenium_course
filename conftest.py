import pytest, os, allure
from datetime import datetime
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium import webdriver


pytest_plugins = [
   "tests.api.fixtures_api"
]


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome', help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='ru, en', help="Choose language: 'ru' or 'en'")

def browser_chrome_settings(request):
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
    
    browser = webdriver.Chrome(options = options, service=Service())
    browser.set_window_size(1280, 720)
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



# Скриншот упавших тестов
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Перехватывает результат теста и делает скриншот при падении.
    """
    # Получаем результат выполнения теста
    outcome = yield
    rep = outcome.get_result()

    # Проверяем, что тест упал (failed) и это стадия call (основное выполнение теста)
    if rep.when == "call" and rep.failed:
        # Проверяем, есть ли в тесте фикстура browser, что можно делать скриншот чего-то
        browser = None
        for fixture in item.fixturenames:
            if fixture == "browser":
                browser = item.funcargs.get("browser")
                break

        if browser:
            try:
                # Генерируем имя файла с временной меткой
                timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                screenshot_name = f"screenshot_error_{timestamp}.png"
                screenshot_path = os.path.join("screenshots", screenshot_name)

                # Создаём директорию для скриншотов, если её нет
                os.makedirs("screenshots", exist_ok=True)

                # Делаем скриншот
                browser.save_screenshot(screenshot_path)

                # Прикрепляем скриншот к отчёту Allure
                with open(screenshot_path, "rb") as image_file:
                    allure.attach(
                        body=image_file.read(),
                        name=f"Screenshot_error_{timestamp}",
                        attachment_type=allure.attachment_type.PNG
                    )
                print(f"Screenshot saved at {screenshot_path} and attached to Allure report")
            except Exception as e:
                print(f"Failed to take screenshot: {e}")