import pytest


@pytest.mark.usefixtures("setup")
class TestVerifyTitle:
    def test_verifyTitle(self):
        pageTitle = self.driver.title
        print('The page Title is : ', pageTitle)
        assert "OrangeHRM" in pageTitle

# driver.implicitly_wait(5)
