import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from Config.config import get_chromedriver_path


@pytest.fixture(scope='class')
def init_driver(request):
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-extensions")
    web_driver = webdriver.Chrome(executable_path=get_chromedriver_path(),
                                  options=chrome_options)
    request.cls.driver = web_driver
    yield
    web_driver.close()
