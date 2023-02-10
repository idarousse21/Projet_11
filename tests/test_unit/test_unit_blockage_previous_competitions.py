from freezegun import freeze_time
from server import get_future_competitions
import pytest


class TestUnitPastCompetition:
    @pytest.mark.parametrize(
        "datetime,number_competition",
        [("2023-01-14", 2), ("2022-05-14", 3), ("2025-01-20", 0)],
    )
    def test_future_competition_competitions_2023_01_14(
        self, datetime, number_competition
    ):
        with freeze_time(datetime):
            assert number_competition == len(get_future_competitions())
