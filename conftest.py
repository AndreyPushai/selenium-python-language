import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

supported_browsers = {
        'chrome' : webdriver.Chrome,
        'firefox' : webdriver.Firefox
        }

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None, help="You should enter --browser_name={name of the browser}")
    parser.addoption('--language', action='store', default=None, help="You should enter --language=en")
    

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption('browser_name')
    language = request.config.getoption('language')

    if browser_name in supported_browsers:
        browser = supported_browsers.get(browser_name)()
        print(f"\n Starting {browser_name} browser for test...")

        if browser == 'chrome':
            options = Options()
            options.add_experimental_option('prefs', {'intl.accept_languages': language})
            browser = webdriver.Chrome(options=options)
        elif browser == 'firefox':
            fp = webdriver.FirefoxProfile()
            fp.set_preference("intl.accept_languages", language)
            browser = webdriver.Firefox(firefox_profile=fp)

    else:
        joined_browsers = ', '.join(supported_browsers.keys())
        raise pytest.UsageError(f"--browser_name is invalid, supported browsers: {joined_browsers}")

    yield browser
    print("\n Quiting browser...")
    browser.quit()
