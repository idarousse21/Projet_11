import pytest
from server import app
import server


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
    data_user = [
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
    return data_user


@pytest.fixture
def data_base_mocker(mocker, data_users, data_competitions):
    mocker.patch.object(server, "clubs", data_users)
    mocker.patch.object(server, "competitions", data_competitions)


@pytest.fixture
def message_response():
    message = {
        "less_zero": "The number of seats purchased cannot be less than 1",
        "less_club_point": "The club points balance is lower than the places bought.",
        "less_competition_point": "The places to ask for are superior to the places available in the competition.",
        "purchases_valid": "Great-booking complete!",
    }
    return message
