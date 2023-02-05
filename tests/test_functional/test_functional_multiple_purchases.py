from selenium.webdriver.common.by import By
import pytest
import random
import time


def function_purchases(driver, number_places):
    time.sleep(4)
    driver.find_element(By.LINK_TEXT, "Book Places").click()
    driver.find_element(By.CSS_SELECTOR, "input[name='places']").send_keys(
        number_places
    )
    driver.find_element(By.TAG_NAME, "button").click()
    return driver


class TestMultiplePurchase:
    def test_multiple_purchase_valid(self, driver_multiple_purchase):
        purchases = 4
        club_purchase = 0
        while club_purchase < 12:
            club_purchase += purchases
            response = function_purchases(driver_multiple_purchase, purchases)
        message = f"Purchases club: {str(club_purchase)}"
        assert message in response.find_elements(By.TAG_NAME, "li")[1].text

    def test_multiple_purchase_invalid(self, driver_multiple_purchase):
        purchases = 5
        club_purchase = 0
        for _ in range(3):
            club_purchase += purchases
            response = function_purchases(driver_multiple_purchase, purchases)
        message = "You cannot buy more than 12 places for this competition."

        assert message == response.find_elements(By.TAG_NAME, "li")[
            0
        ].text
