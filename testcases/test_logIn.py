import time

import pytest
from selenium.webdriver.common.by import By

from pages.hrm_logInPage import LogInPage


@pytest.mark.usefixtures("setup")
class TestLogIn:
    def test_logIn(self):

        lp = LogInPage(self.driver)
        lp.logIn("orange", "orangepassword123")
        lp.clickLogInBtn()

        welcomeText = self.driver.find_element(By.XPATH, "//div[@id='branding']/a[2]").text
        time.sleep(2)
        assert "Welcome" in welcomeText
        print('User Log in Successful')
