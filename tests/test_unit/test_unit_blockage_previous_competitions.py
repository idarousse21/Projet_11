from freezegun import freeze_time
from server import get_future_competitions


class TestUnitPastCompetition:
    @freeze_time("2023-01-14")
    def test_future_competition_competitions_2023_01_14(self):
        assert 2 == len(get_future_competitions())

    @freeze_time("2022-05-14")
    def test_future_competition_competitions_2022_05_14(self):
        assert 3 == len(get_future_competitions())

    @freeze_time("2025-01-20")
    def test_future_competition_competitions_2025_01_20(self):
        assert 0 == len(get_future_competitions())
