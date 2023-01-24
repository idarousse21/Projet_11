import pytest
from server import app
from selenium import webdriver


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


@pytest.fixture
def message():
    data_message = {"invalid": "The email is incorrect.", "valid": "Welcome, "}
    return data_message

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:5000/")
    yield driver
    driver.close()
