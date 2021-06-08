import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from Config.config import TestConfig


@pytest.fixture(scope='class')
def init_driver(request):
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-extensions")
    web_driver = webdriver.Chrome(executable_path=TestConfig.CHROME_DRIVER_PATH,
                                  options=chrome_options)
    request.cls.driver = web_driver
    yield
    web_driver.close()
