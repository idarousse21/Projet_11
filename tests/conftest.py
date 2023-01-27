import pytest
from server import app
from selenium import webdriver


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client




@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:5000/")
    yield driver
    driver.close()
