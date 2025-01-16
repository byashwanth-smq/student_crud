import pytest
from app.services.user_service import UserService
from app.models.user import User
from unittest.mock import Mock

class TestUserService:
    @pytest.fixture
    def mock_db_handler(self):
        return Mock()

    @pytest.fixture
    def user_service(self, mock_db_handler):
        return UserService(db_handler=mock_db_handler)

    def test_create_user(self, user_service, mock_db_handler):
        # Arrange
        mock_user = Mock(spec=User)
        mock_user.to_dict.return_value = {
            'id': 1,
            'username': 'test_user',
            'email': 'test@example.com',
            'created_at': '2023-09-15T00:00:00',
            'updated_at': '2023-09-15T00:00:00'
        }
        mock_db_handler.create_user.return_value = mock_user

        # Act
        result = user_service.create_user('test_user', 'test@example.com')

        # Assert
        assert result == mock_user.to_dict()
        mock_db_handler.create_user.assert_called_once_with('test_user', 'test@example.com')

    def test_get_user(self, user_service, mock_db_handler):
        # Arrange
        mock_user = Mock(spec=User)
        mock_user.to_dict.return_value = {
            'id': 1,
            'username': 'test_user',
            'email': 'test@example.com',
            'created_at': '2023-09-15T00:00:00',
            'updated_at': '2023-09-15T00:00:00'
        }
        mock_db_handler.get_user.return_value = mock_user

        # Act
        result = user_service.get_user(1)

        # Assert
        assert result == mock_user.to_dict()
        mock_db_handler.get_user.assert_called_once_with(1)

    def test_get_all_users(self, user_service, mock_db_handler):
        # Arrange
        mock_user = Mock(spec=User)
        mock_user.to_dict.return_value = {
            'id': 1,
            'username': 'test_user',
            'email': 'test@example.com',
            'created_at': '2023-09-15T00:00:00',
            'updated_at': '2023-09-15T00:00:00'
        }
        mock_db_handler.get_all_users.return_value = [mock_user]

        # Act
        result = user_service.get_all_users()

        # Assert
        assert result == [mock_user.to_dict()]
        mock_db_handler.get_all_users.assert_called_once()

    def test_update_user(self, user_service, mock_db_handler):
        # Arrange
        mock_user = Mock(spec=User)
        mock_user.to_dict.return_value = {
            'id': 1,
            'username': 'updated_user',
            'email': 'test@example.com',
            'created_at': '2023-09-15T00:00:00',
            'updated_at': '2023-09-15T00:00:00'
        }
        mock_db_handler.update_user.return_value = mock_user

        # Act
        result = user_service.update_user(1, username='updated_user')

        # Assert
        assert result == mock_user.to_dict()
        mock_db_handler.update_user.assert_called_once_with(1, username='updated_user', email=None)

    def test_delete_user(self, user_service, mock_db_handler):
        # Arrange
        mock_db_handler.delete_user.return_value = True

        # Act
        result = user_service.delete_user(1)

        # Assert
        assert result is True
        mock_db_handler.delete_user.assert_called_once_with(1)