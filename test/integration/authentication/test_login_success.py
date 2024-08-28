import pytest


class TestIntegrationLoginSuccess:
    host_create_user: str = "/api/authentication/user/register"
    host_login: str ="/api/authentication/login"
    request: dict = {
        "username": "existinguser",
        "email": "existing@jojotest.com",
        "password": "ValidPass123!"
    }
    login_request: dict = {
        "username": "existinguser",
        "password": "ValidPass123!"
    }

    @pytest.fixture(autouse=True)
    def setup_method(self, test_client):
        """Create a user in the database before the test."""
        # Make a request to create the user
        response = test_client.post(self.host_create_user, json=self.request)
        assert response.status_code == 201  # Ensure the user was created successfully

    def test_login(self, test_client):
        """Test the registration of an already existing user."""
        # Attempt to register the same user again
        response_exception = test_client.post(
            self.host_login, json=self.login_request)
        response_json = response_exception.json()
        assert response_exception.status_code == 200
        assert isinstance(response_json.get("access_token"), str)
        assert response_json.get("token_type") == "Bearer"