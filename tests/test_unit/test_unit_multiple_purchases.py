import pytest
from server import dictionary_purchases, dictionary_purchases_update


class TestUnitMultiplePurchases:
    def test_dictionary_purchases(self, data_users, data_competitions):
        dictionary_purchases_club = dictionary_purchases(data_users, data_competitions)
        dictionary = {}
        for club in data_users:
            dictionary[club["email"]] = {}
            for comp in data_competitions:
                dictionary[club["email"]][comp["name"]] = 0
        assert dictionary == dictionary_purchases_club

    def test_dictionary_purchases_update(
        self, data_users, data_competitions, data_purchases_clubs
    ):
        purchases = 5
        club_email = data_users[0]["email"]
        comp = data_competitions[0]["name"]
        dictionary_update = dictionary_purchases_update(
            data_purchases_clubs, club_email, comp, purchases
        )
        assert data_purchases_clubs == dictionary_update
