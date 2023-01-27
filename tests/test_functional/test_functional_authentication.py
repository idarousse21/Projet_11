from selenium.webdriver.common.by import By
import time
import pytest


class TestFunctionalAuthentication:
    @pytest.mark.parametrize(
        "user_mail, message,",
        [
            ("test@test.com", "The email is incorrect."),
            ("admin@irontemple.com", "Welcome, "),
        ],
    )
    def test_authentication_(self, driver, user_mail, message):
        driver.find_element(By.TAG_NAME, "input").send_keys(user_mail)
        driver.find_element(By.TAG_NAME, "button").click()
        time.sleep(1)
        if user_mail == "admin@irontemple.com":
            assert (message + user_mail) in driver.find_elements(By.TAG_NAME, "h2")[
                0
            ].text
        else:
            assert message in driver.find_elements(By.TAG_NAME, "li")[0].text
