import pytest


class TestIntegrationRegisterUseErrorPassword:
    host: str = "/api/authentication/user/register"

    @pytest.mark.parametrize("password, expected_status, expected_detail", [
        ("short", 422, "Password must be at least 8 characters long."),
        ("noSpecialChars1", 422, "Password must contain at least one special character."),
        ("NOLOWERCASE1!", 422,
         "Password must contain at least one uppercase and one lowercase letter."),
        ("noSpecialChars", 422, "Password must contain at least one number."),
        ("password", 422, "Password is too common."),
        ("123456", 422, "Password is too common."),
        ("123456789", 422, "Password is too common."),
        ("qwerty", 422, "Password is too common."),
        ("abc123", 422, "Password is too common."),
        ("0123456789", 422, "Password cannot contain simple sequences."),
        ("abcdefghijklmnopqrstuvwxyz", 422, "Password cannot contain simple sequences."),
        ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 422, "Password cannot contain simple sequences."),
    ])
    def test_password_validation(self, test_client, password, expected_status, expected_detail):
        """Test various password validation rules."""
        request = {
            "username": "testuser",
            "email": "test@jojotest.com",
            "password": password
        }

        response = test_client.post(self.host, json=request)
        assert response.status_code == expected_status
        result = response.json()
        assert result.get("detail") == expected_detail
