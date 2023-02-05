from selenium.webdriver.common.by import By
import pytest


def login_to_the_site(driver, user_mail):

    driver.find_element(By.TAG_NAME, "input").send_keys(user_mail)
    driver.find_element(By.TAG_NAME, "button").click()
    return driver


class TestFunctionalAuthentication:
    @pytest.mark.parametrize(
        "user_mail, message,",
        [
            ("admin@irontemple.com", "Welcome, "),
        ],
    )
    def test_authentication_valid(self, driver, user_mail, message):
        response = login_to_the_site(driver, user_mail)
        assert (message + user_mail) in response.find_elements(By.TAG_NAME, "h2")[
            0
        ].text

    @pytest.mark.parametrize(
        "user_mail, message,",
        [
            ("test@test.com", "The email is incorrect."),
        ],
    )
    def test_authentication_invalid(self, driver, user_mail, message):
        response = login_to_the_site(driver, user_mail)
        assert message in response.find_elements(By.TAG_NAME, "li")[0].text
