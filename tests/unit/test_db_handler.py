import pytest
from app.db.db_handler import DBHandler
from app.models.user import User
from sqlalchemy.exc import IntegrityError

def test_create_user(client, mock_db_session):
    """Test creating a user"""
    handler = DBHandler()
    user = handler.create_user('test_user', 'test@example.com')
    
    assert isinstance(user, User)
    assert user.username == 'test_user'
    assert user.email == 'test@example.com'
    mock_db_session.add.assert_called_once()
    mock_db_session.commit.assert_called_once()

def test_create_user_duplicate(client, mock_db_session):
    """Test creating a user with duplicate username/email"""
    mock_db_session.commit.side_effect = IntegrityError(None, None, None)
    
    handler = DBHandler()
    with pytest.raises(IntegrityError):
        handler.create_user('test_user', 'test@example.com')
    
    mock_db_session.rollback.assert_called_once()

def test_get_user(client):
    """Test getting a user"""
    # First create a user
    handler = DBHandler()
    created_user = handler.create_user('test_user', 'test@example.com')
    
    # Then get the user
    user = handler.get_user(created_user.id)
    assert user.username == 'test_user'
    assert user.email == 'test@example.com'

def test_get_all_users(client):
    """Test getting all users"""
    handler = DBHandler()
    handler.create_user('user1', 'user1@example.com')
    handler.create_user('user2', 'user2@example.com')
    
    users = handler.get_all_users()
    assert len(users) == 2
    assert users[0].username == 'user1'
    assert users[1].username == 'user2'

def test_update_user(client):
    """Test updating a user"""
    handler = DBHandler()
    user = handler.create_user('test_user', 'test@example.com')
    
    updated_user = handler.update_user(user.id, username='updated_user')
    assert updated_user.username == 'updated_user'
    assert updated_user.email == 'test@example.com'

def test_delete_user(client):
    """Test deleting a user"""
    handler = DBHandler()
    user = handler.create_user('test_user', 'test@example.com')
    
    result = handler.delete_user(user.id)
    assert result is True