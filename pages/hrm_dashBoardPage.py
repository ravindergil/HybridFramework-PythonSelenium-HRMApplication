from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class DashBoardPage():
    def __init__(self, driver):
        self.driver = driver

    def clickAddEmp(self):
        action = ActionChains(self.driver)
        webElementPIM = self.driver.find_element(By.LINK_TEXT, "PIM")
        action.move_to_element(webElementPIM).perform()
        self.driver.find_element(By.LINK_TEXT, "Add Employee").click();