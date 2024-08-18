import pytest


class TestIntegrationRegisterUseErrorEmail:
    host: str = "/api/authentication/user/register"

    @pytest.mark.parametrize("email, expected_status, expected_detail", [
        ("teste@example.com", 422, "Email domain is not allowed."),
        ("teste@test.com", 422, "Email domain is not allowed."),
    ])
    def test_email_validation(self, test_client, email, expected_status, expected_detail):
        """Test various eamil validation rules."""
        request = {
            "username": "testuser",
            "email": email,
            "password": "ValidPass123!"
        }

        response = test_client.post(self.host, json=request)
        assert response.status_code == expected_status
        result = response.json()
        assert result.get("detail") == expected_detail
