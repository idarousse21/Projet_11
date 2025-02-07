import pytest
from server import app
import server
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


@pytest.fixture
def data_users():
    data_users = [
        {
            "name": "test_club_1",
            "email": "test1@club.com",
            "points": "25",
        },
        {
            "name": "test_club_2",
            "email": "test2@club.com",
            "points": "3",
        },
        {
            "name": "test_club_3",
            "email": "test3@club.com",
            "points": "10",
        },
    ]
    return data_users


@pytest.fixture
def data_competitions():
    data_competitions = [
        {
            "name": "test_competition_1",
            "date": "2020-10-22 13:30:00",
            "numberOfPlaces": "13",
        },
        {
            "name": "test_competition_2",
            "date": "2020-10-22 13:20:00",
            "numberOfPlaces": "5",
        },
    ]
    return data_competitions


@pytest.fixture
def data_purchases_clubs():
    data_purchases_clubs = {
        "test1@club.com": {"test_competition_1": 0, "test_competition_2": 0},
        "test2@club.com": {"test_competition_1": 0, "test_competition_2": 0},
        "test3@club.com": {"test_competition_1": 0, "test_competition_2": 0},
    }
    return data_purchases_clubs


@pytest.fixture
def message_response():
    message = {
        "less_zero": "The number of seats purchased cannot be less than 1",
        "less_club_point": "The club points balance is lower than the places bought.",
        "less_competition_point": "The places to ask for are superior to the places available in the competition.",
        "purchases_valid": "Great-booking complete!",
    }
    return message


@pytest.fixture
def data_base_mocker(mocker, data_users, data_competitions, data_purchases_clubs):
    mocker.patch.object(server, "clubs", data_users)
    mocker.patch.object(server, "competitions", data_competitions)
    mocker.patch.object(server, "clubs_purchase", data_purchases_clubs)


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("http://127.0.0.1:5000/")
    yield driver
    driver.close()


@pytest.fixture
def driver_tests_valid_purchase():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:5000/")
    user_mail = "kate@shelifts.co.uk"
    driver.find_element(By.TAG_NAME, "input").send_keys(user_mail)
    driver.find_element(By.TAG_NAME, "button").click()
    yield driver
    driver.close()


@pytest.fixture
def driver_multiple_purchase():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:5000/")
    user_mail = "john@simplylift.co"
    driver.find_element(By.TAG_NAME, "input").send_keys(user_mail)
    driver.find_element(By.TAG_NAME, "button").click()
    yield driver
    driver.close()
