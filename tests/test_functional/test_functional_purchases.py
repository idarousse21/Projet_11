from selenium.webdriver.common.by import By


class TestPurchase:
    def test_invalid_and_valid_purchases(self, driver, message_response):
        driver.find_element(By.TAG_NAME, "ul").find_element(
            By.TAG_NAME, "li"
        ).find_element(By.LINK_TEXT, "Book Places").click()
        driver.find_element(By.CSS_SELECTOR, "input[name='places']").send_keys(5)
        driver.find_element(By.TAG_NAME, "button").click()
        assert (
            message_response["less_club_point"]
            in driver.find_elements(By.TAG_NAME, "li")[0].text
        )
        driver.find_element(By.CSS_SELECTOR, "input[name='places']").send_keys(0)
        driver.find_element(By.TAG_NAME, "button").click()
        assert (
            message_response["less_zero"]
            in driver.find_elements(By.TAG_NAME, "li")[0].text
        )
        driver.find_element(By.CSS_SELECTOR, "input[name='places']").send_keys(2)
        driver.find_element(By.TAG_NAME, "button").click()
        assert (
            message_response["purchases_valid"]
            in driver.find_elements(By.TAG_NAME, "li")[0].text
        )
