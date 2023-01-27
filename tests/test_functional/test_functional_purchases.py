from selenium.webdriver.common.by import By
import pytest


def function_purchases(cls, driver, number_places):
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
        (5, "The club points balance is lower than the places bought."),
        (0, "The number of seats purchased cannot be less than 1"),
    )
    def test_invalid_purchases(self, driver, number_places, message):
        response = function_purchases(driver, number_places)
        assert (
            message["less_club_point"]
            in response.find_elements(By.TAG_NAME, "li")[0].text
        )

        # driver.find_element(By.CSS_SELECTOR, "input[name='places']").send_keys(2)
        # driver.find_element(By.TAG_NAME, "button").click()
        # assert (
        #     message_response["purchases_valid"]
        #     in driver.find_elements(By.TAG_NAME, "li")[0].text
        # )
