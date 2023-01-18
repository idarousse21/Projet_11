import pytest
from http import HTTPStatus
from server import app, valid_purchase



class TestValidPurchase:

    @pytest.mark.parametrize("places_required,number_places_competition, number_places_club,boolean, message",
        [
            (2,25,4,True,"Great-booking complete!"),
            (13,25,50,False,"You cannot reserve more than 12 places in a competition."),
            (10,50,5,False,"The club's points balance is lower than the places bought."),
            (0,10,7,False,"The number of seats purchased cannot be less than 1"),
            (10,5,70,False,"The places to ask for are superior to the places available in the competition.")])
    def test_valid_purchase(self,places_required,number_places_competition, number_places_club,boolean,message):
        purchase = valid_purchase(places_required, number_places_competition, number_places_club)
        assert purchase[0] == boolean
        assert message == purchase[1]

