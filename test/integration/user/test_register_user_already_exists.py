import pytest

class TestIntegrationRegisterUseAlreadyExists:
    host: str = "/api/authentication/user/register"
    request: dict = {
        "username": "existinguser",
        "email": "existing@jojotest.com",
        "password": "ValidPass123!"
    }

    @pytest.fixture(autouse=True)
    def setup_method(self, test_client):
        """Create a user in the database before the test."""
        # Make a request to create the user
        response = test_client.post(self.host, json=self.request)
        assert response.status_code == 201  # Ensure the user was created successfully

    def test_user_registration(self, test_client):
        """Test the registration of an already existing user."""
        # Attempt to register the same user again
        response_exception = test_client.post(self.host, json=self.request)
        assert response_exception.status_code == 409
        assert response_exception.json() == {"detail": "Username or email already exists"}
