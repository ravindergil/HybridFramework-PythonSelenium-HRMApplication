import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup")
class TestGetHeaderUrl:
    def test_getHeaderUrl(self):
        HeaderURL = self.driver.find_element(By.XPATH, "//div[@id='divLogo']/img").get_attribute("src")
        print("Header URL : ", HeaderURL)
        assert "orangehrm" in HeaderURL


