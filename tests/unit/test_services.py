import pytest
from unittest.mock import MagicMock, patch
from app.db.db_handler import DBHandler
from app.models.user import UserDB
from app.services.user_service import UserService
from app.models.user import User
from unittest.mock import Mock

class TestUserService:
    @pytest.fixture
    def mock_db_handler(self):
        return MagicMock(spec=DBHandler)

    @pytest.fixture
    def user_service(self, mock_db_handler):
        return UserService(db_handler=mock_db_handler)

    @patch("app.models.user.UserResponse.model_validate")
    def test_create_user(self, user_service, mock_db_handler):
        # Arrange
        mock_user_data = {
            'id': 1,
            'username': 'test_user',
            'email': 'test@example.com',
            'created_at': '2023-09-15T00:00:00',
            'updated_at': '2023-09-15T00:00:00'
        }
        
        model_user = UserDB(**mock_user_data)
        service_user = user_service.create_user(mock_user_data)
        model_user == service_user
        # mock_db_handler.create_user.return_value = mocked_user  # mock db handler
        # mock_db_handler.create_user.assert_called_once()
        # soome, message = user_service.create_user(**mock_user_data)
        # assert message == 'created successfully'
        # assert username == mocked_user.username
        # mock_db_handler.create_user.assert_called_once()
        # user_data = User(name='test_user', email='test@example.com')
        # # Act
        # result = user_service.create_user(user_data)

        # # Assert
        # assert result == mock_user.to_dict()  # Check if result is the dict
        # mock_db_handler.create_user.assert_called_once_with('test_user', 'test@example.com')
 
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