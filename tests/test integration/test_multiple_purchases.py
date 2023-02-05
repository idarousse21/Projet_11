from http import HTTPStatus

HTTP_OK = HTTPStatus.OK
HTTP_BAD_REQUEST = HTTPStatus.BAD_REQUEST


class TestMultiplePurchase:
    def test_multiple_purchases_valid(
        self,
        client,
        data_base_mocker,
        data_users,
        data_competitions,
        data_purchases_clubs,
    ):
        club_email = data_users[0]["email"]
        comp = data_competitions[0]["name"]
        data_purchases_clubs[club_email][comp] = 7
        data = {
            "competition": data_competitions[0]["name"],
            "club": data_users[0]["name"],
            "places": 5,
        }
        response = client.post("/purchasePlaces", data=data)
        assert response.status_code == HTTP_OK
        assert "Great-booking complete!" in response.data.decode()
        assert str(data_purchases_clubs[club_email][comp]) in response.data.decode()

    def test_multiple_purchases_invalid(
        self,
        client,
        data_base_mocker,
        data_users,
        data_competitions,
        data_purchases_clubs,
    ):
        club_email = data_users[0]["email"]
        comp = data_competitions[0]["name"]
        data_purchases_clubs[club_email][comp] = 8
        data = {
            "competition": data_competitions[0]["name"],
            "club": data_users[0]["name"],
            "places": 5,
        }
        response = client.post("/purchasePlaces", data=data)
        assert (
            "You cannot buy more than 12 places for this competition."
            in response.data.decode()
        )
