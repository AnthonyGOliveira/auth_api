# tests/test_user.py
from datetime import datetime, timezone

class TestIntegrationRegisterUseCaseSuccess:
    host: str = "/api/authentication/user/register"    

    def test_execute(self, test_client):
        request = {
            "username": "anthonygdos",
            "email": "teste@gmail.com",
            "password": "ValidPass123!"
        }
        response = test_client.post(self.host, json=request)
        now = datetime.now(timezone.utc)
        expected_response = {
            "username": "anthonygdos",
            "email": "teste@gmail.com",
            "is_active": True,
            "created_at": now.isoformat()  # Ensure expected response is in ISO format
        }
        response_json = response.json()
        assert response.status_code == 201
        assert response_json["username"] == expected_response["username"]
        assert response_json["email"] == expected_response["email"]
        assert response_json["is_active"] == expected_response["is_active"]
        created_at_str = response_json.get("created_at")
        created_at = datetime.fromisoformat(created_at_str).astimezone(
            timezone.utc)  # Ensure timezone-aware
        expected_created_at = datetime.fromisoformat(
            expected_response["created_at"]).astimezone(timezone.utc)  # Ensure timezone-aware
        delta = expected_created_at - created_at
        assert delta.total_seconds() < 1  # Allow for slight variations in time
