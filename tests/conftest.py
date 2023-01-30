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
    data_user = [
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
    return data_user


@pytest.fixture
def data_competitions():
    data_competition = [
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
    return data_competition


@pytest.fixture
def data_purchases_clubs():
    data_purchases_clubs = {
        "test1@club.com": {"test_competition_1": 0, "test_competition_2": 0},
        "test2@club.com": {"test_competition_1": 0, "test_competition_2": 0},
        "test3@club.com": {"test_competition_1": 0, "test_competition_2": 0},
    }
    return data_purchases_clubs


@pytest.fixture
def data_base_mocker(mocker, data_users, data_competitions, data_purchases_clubs):
    mocker.patch.object(server, "clubs", data_users)
    mocker.patch.object(server, "competitions", data_competitions)
    mocker.patch.object(server, "clubs_purchase", data_purchases_clubs)


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:5000/")
    user_mail = "john@simplylift.co"
    driver.find_element(By.TAG_NAME, "input").send_keys(user_mail)
    driver.find_element(By.TAG_NAME, "button").click()
    yield driver
    driver.close()
