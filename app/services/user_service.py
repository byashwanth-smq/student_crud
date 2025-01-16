from app.db.db_handler import DBHandler
from app.models.user import User, UserUpdate, UserResponse, UserList
from typing import List

class UserService:
    def __init__(self, db_handler: DBHandler = None):
        self.db_handler = db_handler or DBHandler()

    def create_user(self, user_data: User) -> UserResponse:
        """Create a new user"""
        user = self.db_handler.create_user(user_data)
        return UserResponse.model_validate(user)

    def get_user(self, user_id: int) -> UserResponse:
        """Get user by ID"""
        user = self.db_handler.get_user(user_id)
        return UserResponse.model_validate(user)

    def get_all_users(self) -> UserList:
        """Get all users"""
        users = self.db_handler.get_all_users()
        return UserList(
            users=[UserResponse.model_validate(user) for user in users],
            total=len(users)
        )

    def update_user(self, user_id: int, user_data: UserUpdate) -> UserResponse:
        """Update user details"""
        user = self.db_handler.update_user(user_id, user_data)
        return UserResponse.model_validate(user)

    def delete_user(self, user_id: int) -> bool:
        """Delete a user"""
        return self.db_handler.delete_user(user_id)