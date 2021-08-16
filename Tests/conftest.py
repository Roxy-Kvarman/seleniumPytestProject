import os
from datetime import datetime

import pytest
from selenium import webdriver
from Config.config import Config
from Pages.WelcomePage import WelcomePage
from Pages.BasePage import BasePage
from Utilities.logger import Logger
from Utilities.browser import Browser


@pytest.fixture(scope='session', autouse=True)
def init_driver(request):
    print("---------------------set up-----------------------")
    # if request.param == "chrome":
    #     driver = webdriver.Chrome(executable_path=Config.chrome_driver_pagh)
    # if request.param == "firefox":
    #     driver = webdriver.Firefox(executable_path=Config.firefox_driver_path)
    driver = Browser.get_driver()
    # request.cls.driver = driver
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get(Config.base_url)
    welcome_page = WelcomePage()
    if not BasePage.isLogin:
        Logger.logger.info("Navigate to Login Page")
        login_page = welcome_page.navigate_to_login_page()
        Logger.logger.info("Log in with email: " + Config.email + ", and password: " + Config.password)
        login_page.login(Config.email, Config.password)
        BasePage.isLogin = True
    else:
        Logger.logger.info("Already Logged in")
        welcome_page.navigate_to_dashboard_page()

    yield
    print("--------------------tear down---------------------")
    BasePage.isLogin = False
    driver.close()
    driver.quit()
    Browser.kill_driver_process("chrome")


@pytest.fixture(autouse=True)
def get_test_name():
    test_name = os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0]
    return test_name

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):

    timestamp = datetime.now().strftime('%H-%M-%S')

    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call':

        feature_request = item.funcargs['request']

        driver = Browser.get_driver()
        driver.save_screenshot('C:\\Users\\roxyk\\PycharmProjects\\seleniumPytestProject\\Reports\\scr'+timestamp+'.png')

        extra.append(pytest_html.extras.image('C:\\Users\\roxyk\\PycharmProjects\\seleniumPytestProject\\Reports\\scr'+timestamp+'.png'))

        # always add url to report
        extra.append(pytest_html.extras.url('C:\\Users\\roxyk\\PycharmProjects\\seleniumPytestProject\\Reports\\scr'+timestamp+'.png'))
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            extra.append(pytest_html.extras.image('C:\\Users\\roxyk\\PycharmProjects\\seleniumPytestProject\\Reports\\scr.png'))
            extra.append(pytest_html.extras.html('<div>Additional HTML</div>'))
        report.extra = extra



