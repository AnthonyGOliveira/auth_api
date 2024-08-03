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
            "password": "123456789"
        }
        response = self.client.post(self.host, json=request)
        expected_response = {
            "username": "anthonygdos",
            "email": "teste@gmail.com",
            "password": "123456789"
        }
        assert response.status_code == 201
        assert response.json() == expected_response
