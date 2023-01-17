import pytest
from http import HTTPStatus
from server import app
from flask import flash

HTTP_OK = HTTPStatus.OK
HTTP_UNAUTHORIZED = HTTPStatus.UNAUTHORIZED
ENDPOINT_SHOWSUMMARY = "/showSummary"

class TestAuthenticationEmail:
    
    def test_should_status_code_ok(self,client):
        response = client.get('/')
        assert response.status_code == HTTP_OK


    @pytest.mark.parametrize("email, status_code", [
        ({'email': 'admin@irontemple.com'}, HTTP_OK),
        ({'email': 'bad@mail.com'}, HTTP_UNAUTHORIZED)])
    def test_authenticate(self,client,email,status_code):
        response= client.post(ENDPOINT_SHOWSUMMARY, data=email)
        if response.status_code == HTTP_OK:
            message = f"Welcome, {email['email']}"
            assert response.status_code == status_code
            assert message in response.data.decode()
        elif response.status_code == HTTP_UNAUTHORIZED:
            assert response.status_code == status_code
            assert "Redirecting" in response.data.decode()

