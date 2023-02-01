from selenium import webdriver
from selenium.webdriver.common.by import By
from server import clubs


def test_display_point():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:5000/")
    driver.find_element(By.LINK_TEXT, "View points by club").click()
    for club in clubs:
        assert club["name"] and club["points"] in driver.find_element(By.TAG_NAME, "table").text
