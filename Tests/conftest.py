import pytest
from selenium import webdriver

from Config.config import TestConfig


@pytest.fixture(scope='class')
def init_driver(request):
    web_driver = webdriver.Chrome(executable_path=TestConfig.CHROME_DRIVER_PATH)
    request.cls.driver = web_driver
    yield
    web_driver.close()
