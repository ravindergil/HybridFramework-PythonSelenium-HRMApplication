import time

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from pages.hrm_dashBoardPage import DashBoardPage
from pages.hrm_logInPage import LogInPage


@pytest.mark.usefixtures("setup")
class TestAddEmployee:
    def test_addEmployee(self):
        lp = LogInPage(self.driver)
        lp.logIn("orange", "orangepassword123")
        lp.clickLogInBtn()

        time.sleep(3)

        db = DashBoardPage(self.driver)
        db.clickAddEmp()
