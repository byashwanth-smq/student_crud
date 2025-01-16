import pytest
from app.schemas.user import User, UserUpdate, UserResponse
from datetime import datetime

class TestUserSchemas:
    def test_user_create_valid(self):
        """Test valid user creation schema"""
        user_data = {
            "username": "test_user",
            "email": "test@example.com"
        }
        user = User(**user_data)
        assert user.username == "test_user"
        assert user.email == "test@example.com"

    def test_user_create_invalid_email(self):
        """Test invalid email in user creation schema"""
        user_data = {
            "username": "test_user",
            "email": "invalid_email"
        }
        with pytest.raises(ValueError):
            User(**user_data)

    def test_user_create_invalid_username(self):
        """Test invalid username in user creation schema"""
        user_data = {
            "username": "ab",  # too short
            "email": "test@example.com"
        }
        with pytest.raises(ValueError):
            User(**user_data)

    def test_user_update_partial(self):
        """Test partial user update schema"""
        user_data = {
            "username": "updated_user"
        }
        user = UserUpdate(**user_data)
        assert user.username == "updated_user"
        assert user.email is None

    def test_user_response(self):
        """Test user response schema"""
        user_data = {
            "id": 1,
            "username": "test_user",
            "email": "test@example.com",
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow()
        }
        user = UserResponse(**user_data)
        assert user.id == 1
        assert user.username == "test_user"
        assert user.email == "test@example.com"
        assert isinstance(user.created_at, datetime)
        assert isinstance(user.updated_at, datetime)