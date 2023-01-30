import pytest
from server import purchases_initialization_por_club


class TestUnitMultiplePurchases:
    def test_dictionary_purchases(
        self, data_users, data_competitions, data_purchases_clubs
    ):
        dictionary_purchases_club = purchases_initialization_por_club(
            data_users, data_competitions
        )
        assert data_purchases_clubs == dictionary_purchases_club
