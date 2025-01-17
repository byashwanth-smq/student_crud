"""
This module contains both SQLAlchemy and Pydantic models for the User entity.
"""
from app import db
from datetime import datetime
from pydantic import BaseModel, EmailStr, Field, ConfigDict
from typing import Optional, List
from sqlalchemy.orm import Mapped, mapped_column

# SQLAlchemy Model
class UserDB(db.Model):
    """Database model for User"""
    __tablename__ = 'users'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(db.String(80), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(db.String(120), unique=True, nullable=False)
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self) -> str:
        return f'<User {self.username}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'created_at': str(self.created_at),
            'updated_at': str(self.updated_at),
        }

# Pydantic Models
class User(BaseModel):
    """Base User Schema"""
    username: str = Field(..., min_length=3, max_length=80)
    email: EmailStr = Field(..., max_length=120)

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "username": "john_doe",
                "email": "john@example.com"
            }
        }
    )

class UserUpdate(BaseModel):
    """Schema for updating a user"""
    username: Optional[str] = Field(None, min_length=3, max_length=80)
    email: Optional[EmailStr] = Field(None, max_length=120)

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "username": "john_doe_updated",
                "email": "john_updated@example.com"
            }
        }
    )

class UserResponse(User):
    """Schema for user response"""
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": 1,
                "username": "john_doe",
                "email": "john@example.com",
                "created_at": "2023-09-15T00:00:00",
                "updated_at": "2023-09-15T00:00:00"
            }
        }
    )

class UserList(BaseModel):
    """Schema for list of users response"""
    users: List[UserResponse]
    total: int

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "users": [
                    {
                        "id": 1,
                        "username": "john_doe",
                        "email": "john@example.com",
                        "created_at": "2023-09-15T00:00:00",
                        "updated_at": "2023-09-15T00:00:00"
                    }
                ],
                "total": 1
            }
        }
    )