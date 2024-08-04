from fastapi import FastAPI
from fastapi.testclient import TestClient
from app.main import app


class TestRegisterUseCaseSuccess:
    client: TestClient
    host: str = "/authentication/register"

    def setup_method(self):
        self.client = TestClient(app)

    def test_execute(self):
        request = {
            "username": "anthonygdos",
            "email": "teste@gmail.com",
            "password": "ValidPass123!"
        }
        response = self.client.post(self.host, json=request)
        expected_response = {
            "username": "anthonygdos",
            "email": "teste@gmail.com",
            "password": "ValidPass123!",
            "password_is_valid": True
        }
        response_json = response.json()
        assert response.status_code == 201
        assert response_json["username"] == expected_response["username"]
        assert response_json["email"] == expected_response["email"]
        assert response_json["password"] == expected_response["password"]
        assert response_json["password_is_valid"] == expected_response["password_is_valid"]
        assert type(response_json["hash_password"]) == str
