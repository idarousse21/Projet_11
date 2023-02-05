import pytest
from http import HTTPStatus

HTTP_OK = HTTPStatus.OK
HTTP_FOUND = HTTPStatus.FOUND



class TestAuthenticationEmail:
    def test_should_status_code_ok(self, client):
        response = client.get("/")
        assert response.status_code == HTTP_OK

    @pytest.mark.parametrize(
        "email, status_code, message",
        [
            (
                {"email": "admin@irontemple.com"},
                HTTP_OK,
                "Welcome, admin@irontemple.com",
            ),
            ({"email": "bad@mail.com"}, HTTP_FOUND, "Redirecting"),
        ],
    )
    def test_authenticate(self, client, email, status_code, message):
        response = client.post("/showSummary", data=email)
        assert response.status_code == status_code
        assert message in response.data.decode()
