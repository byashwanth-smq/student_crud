import pytest
from app.models.user import User
from datetime import datetime

class TestUserModel:
    def test_new_user(self):
        """Test creating new user instance"""
        user = User(username='test_user', email='test@example.com')
        assert user.username == 'test_user'
        assert user.email == 'test@example.com'
        assert isinstance(user.created_at, datetime)
        assert isinstance(user.updated_at, datetime)

    def test_user_to_dict(self):
        """Test user to_dict method"""
        user = User(username='test_user', email='test@example.com')
        user_dict = user.to_dict()
        
        assert isinstance(user_dict, dict)
        assert user_dict['username'] == 'test_user'
        assert user_dict['email'] == 'test@example.com'
        assert 'created_at' in user_dict
        assert 'updated_at' in user_dict

    def test_user_repr(self):
        """Test user string representation"""
        user = User(username='test_user', email='test@example.com')
        assert str(user) == '<User test_user>'

    def test_user_unique_constraints(self, init_database):
        """Test unique constraints on username and email"""
        user1 = User(username='test_user', email='test@example.com')
        init_database.session.add(user1)
        init_database.session.commit()

        # Try to create user with same username
        with pytest.raises(Exception):  # You might want to be more specific about the exception
            user2 = User(username='test_user', email='different@example.com')
            init_database.session.add(user2)
            init_database.session.commit()

        init_database.session.rollback()

        # Try to create user with same email
        with pytest.raises(Exception):
            user3 = User(username='different_user', email='test@example.com')
            init_database.session.add(user3)
            init_database.session.commit()