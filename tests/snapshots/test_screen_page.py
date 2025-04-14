import allure

def test_screenshot_main_page(browser, image_regression):
    # Добавляем метаданные для Allure-отчёта: название теста
    allure.dynamic.title("Test Screenshot for Main Page")
    allure.dynamic.description("This test verifies the screenshot of the main page.")
    browser.get("http://selenium1py.pythonanywhere.com/")
    screenshot = browser.get_screenshot_as_png()
    image_regression.check(screenshot)

def test_screenshot_product_page(browser, image_regression):
    # Добавляем метаданные для Allure-отчёта: название теста
    allure.dynamic.title("Test Screenshot for Product Page")
    allure.dynamic.description("This test verifies the screenshot of the product page.")
    browser.get("http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/")
    screenshot = browser.get_screenshot_as_png()
    image_regression.check(screenshot)
    

def test_screenshot_login_page(browser, image_regression):
    # Добавляем метаданные для Allure-отчёта: название теста
    allure.dynamic.title("Test Screenshot for Login Page")
    allure.dynamic.description("This test verifies the screenshot of the login page.")
    browser.get("http://selenium1py.pythonanywhere.com/ru/accounts/login/")
    screenshot = browser.get_screenshot_as_png()
    image_regression.check(screenshot)
