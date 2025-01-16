from app import db
from app.models.user import UserDB, UserUpdate
from sqlalchemy.exc import IntegrityError
from typing import List, Optional

class DBHandler:
    @staticmethod
    def create_user(user_data: any) -> any:
        """Create a new user"""
        user = UserDB(**user_data)
        db.session.add(user)
        try:
            db.session.commit()
            return user
        except IntegrityError:
            db.session.rollback()
            raise

    @staticmethod
    def get_user(user_id: int) -> UserDB:
        """Get user by ID"""
        return UserDB.query.get_or_404(user_id)

    @staticmethod
    def get_all_users() -> List[UserDB]:
        """Get all users"""
        return UserDB.query.all()

    @staticmethod
    def update_user(user_id: int, user_data: UserUpdate) -> UserDB:
        """Update user details"""
        user = UserDB.query.get_or_404(user_id)
        if user_data.username is not None:
            user.username = user_data.username
        if user_data.email is not None:
            user.email = user_data.email
        try:
            db.session.commit()
            return user
        except IntegrityError:
            db.session.rollback()
            raise

    @staticmethod
    def delete_user(user_id: int) -> bool:
        """Delete a user"""
        user = UserDB.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return True