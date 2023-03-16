from selenium.webdriver.common.by import By


class LogInPage():
    def __init__(self, driver):
        self.driver = driver

    def logIn(self, userName, passWord):
        userNameElement = self.driver.find_element(By.ID, "txtUsername")
        userNameElement.send_keys(userName)

        passWordElement = self.driver.find_element(By.ID, "txtPassword")
        passWordElement.send_keys(passWord)

    def clickLogInBtn(self):
        clickLogInElement = self.driver.find_element(By.ID, "btnLogin")
        clickLogInElement.click()
