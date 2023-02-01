from selenium.webdriver.common.by import By
import pytest


def function_purchases(driver, number_places):
    driver.find_element(By.TAG_NAME, "ul").find_element(By.TAG_NAME, "li").find_element(
        By.LINK_TEXT, "Book Places"
    ).click()
    driver.find_element(By.CSS_SELECTOR, "input[name='places']").send_keys(
        number_places
    )
    driver.find_element(By.TAG_NAME, "button").click()
    return driver


class TestPurchase:
    @pytest.mark.parametrize(
        "number_places,message",
        [
            (0, "The number of seats purchased cannot be less than 1"),
        ],
    )
    def test_invalid_purchases(self, driver, number_places, message):
        response = function_purchases(driver, number_places)
        assert (
            message
            in response.find_elements(By.TAG_NAME, "li")[0].text
        )
