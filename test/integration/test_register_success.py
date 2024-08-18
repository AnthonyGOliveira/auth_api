# tests/test_user.py
from app.main import app
from app.dependencies.database_dependency import get_db, get_test_db

class TestIntegrationRegisterUseCaseSuccess:
    host: str = "/api/authentication/user/register"    

    def test_user_registration(self, test_client):
        response = test_client.post(self.host, json={
            "username": "testuser",
            "email": "test@integrationtest.com",
            "password": "(6dgAvbhcj1"
        })
        assert response.status_code == 201
        assert response.json()["username"] == "testuser"
