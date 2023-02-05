from http import HTTPStatus
import random

HTTP_OK = HTTPStatus.OK
HTTP_BAD_REQUEST = HTTPStatus.BAD_REQUEST


class TestPurchase:
    def test_less_club_points(
        self, client, data_base_mocker, data_users, data_competitions, message_response
    ):
        data = {
            "competition": data_competitions[0]["name"],
            "club": data_users[1]["name"],
            "places": 5,
        }
        response = client.post("/purchasePlaces", data=data)
        assert message_response["less_club_point"] in response.data.decode()

    def test_less_competition_points(
        self, client, data_base_mocker, data_users, data_competitions, message_response
    ):
        data = {
            "competition": data_competitions[1]["name"],
            "club": data_users[0]["name"],
            "places": 7,
        }
        response = client.post("/purchasePlaces", data=data)
        assert message_response["less_competition_point"] in response.data.decode()

    def test_less_zero_purchases(
        self, client, data_base_mocker, data_users, data_competitions, message_response
    ):
        data = {
            "competition": data_competitions[1]["name"],
            "club": data_users[0]["name"],
            "places": random.randint(-10, 0),
        }
        response = client.post("/purchasePlaces", data=data)
        assert message_response["less_zero"] in response.data.decode()

    def test_purchases_valid(
        self, client, data_base_mocker, data_users, data_competitions, message_response
    ):
        data = {
            "competition": data_competitions[0]["name"],
            "club": data_users[0]["name"],
            "places": random.randint(1, 12),
        }
        purchase = int(data["places"])
        data_competitions_after_purchase = (
            int(data_competitions[0]["numberOfPlaces"]) - purchase
        )
        data_users_after_purchase = int(data_users[0]["points"]) - purchase
        response = client.post("/purchasePlaces", data=data)

        assert response.status_code == HTTP_OK
        assert message_response["purchases_valid"] in response.data.decode()
        assert str(data_competitions_after_purchase) in response.data.decode()
        assert str(data_users_after_purchase) in response.data.decode()
