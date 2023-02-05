import pytest
from server import valid_purchase


class TestValidPurchase:
    @pytest.mark.parametrize(
        "places_required,number_places_competition, number_places_club,purchases_club,boolean, message",
        [
            (2, 25, 4, 0, True, "Great-booking complete!"),
            (
                10,
                50,
                5,
                0,
                False,
                "The club points balance is lower than the places bought.",
            ),
            (0, 10, 7, 0, False, "The number of seats purchased cannot be less than 1"),
            (
                10,
                5,
                70,
                0,
                False,
                "The places to ask for are superior to the places available in the competition.",
            ),
        ],
    )
    def test_purchase(
        self,
        places_required,
        number_places_competition,
        number_places_club,
        purchases_club,
        boolean,
        message,
    ):
        purchase = valid_purchase(
            places_required,
            number_places_competition,
            number_places_club,
            purchases_club,
        )
        assert purchase[0] == boolean
        assert message == purchase[1]
