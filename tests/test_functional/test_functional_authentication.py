from selenium.webdriver.common.by import By
import time


class TestFunctionalAuthentication:
    def test_authentication_invalid(self, driver, message):
        user_mail = "test@test.com"
        driver.find_element(By.TAG_NAME, "input").send_keys(user_mail)
        driver.find_element(By.TAG_NAME, "button").click()
        time.sleep(1)
        assert message["invalid"] in driver.find_elements(By.TAG_NAME, "li")[0].text
        user_mail = "admin@irontemple.com"
        driver.find_element(By.TAG_NAME, "input").send_keys(user_mail)
        driver.find_element(By.TAG_NAME, "button").click()
        assert (message["valid"] + user_mail) in driver.find_elements(
            By.TAG_NAME, "h2"
        )[0].text
