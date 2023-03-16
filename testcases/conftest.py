import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="class")
def setup(request):
    print("initiating chrome driver")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("http://alchemy.hguy.co/orangehrm")
#    wait = WebDriverWait(driver, 10)
    driver.maximize_window()
    request.cls.driver = driver
#   request.cls.wait = wait

    yield driver
    driver.close()
