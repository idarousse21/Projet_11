from http import HTTPStatus
from server import clubs


class TestIntegrationDisplayPoints:
    def test_display_points(self, client):
        data_clubs = {"clubs": clubs}
        response = client.get("/displayPoints", data=data_clubs)
        assert response.status_code == HTTPStatus.OK
        assert [club["name"] in response.data.decode() for club in clubs]
