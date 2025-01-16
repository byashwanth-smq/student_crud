import json
import pytest
from app.models.user import User

class TestUserRoutes:
    def test_create_user_success(self, client, init_database):
        """Test successful user creation"""
        response = client.post('/api/users/',
                             json={
                                 'username': 'test_user',
                                 'email': 'test@example.com'
                             })
        
        assert response.status_code == 201
        data = json.loads(response.data)
        assert data['username'] == 'test_user'
        assert data['email'] == 'test@example.com'

    def test_create_user_duplicate(self, client, sample_user):
        """Test creating user with duplicate username"""
        response = client.post('/api/users/',
                             json={
                                 'username': 'test_user',
                                 'email': 'different@example.com'
                             })
        
        assert response.status_code == 400
        assert b'Username or email already exists' in response.data

    def test_get_user_success(self, client, sample_user):
        """Test successful user retrieval"""
        response = client.get(f'/api/users/{sample_user.id}')
        
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['username'] == sample_user.username
        assert data['email'] == sample_user.email

    def test_get_user_not_found(self, client, init_database):
        """Test user retrieval for non-existent user"""
        response = client.get('/api/users/999')
        assert response.status_code == 404

    def test_get_all_users(self, client, sample_user):
        """Test getting all users"""
        response = client.get('/api/users/')
        
        assert response.status_code == 200
        data = json.loads(response.data)
        assert isinstance(data, list)
        assert len(data) == 1
        assert data[0]['username'] == sample_user.username

    def test_update_user_success(self, client, sample_user):
        """Test successful user update"""
        response = client.put(f'/api/users/{sample_user.id}',
                            json={'username': 'updated_user'})
        
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['username'] == 'updated_user'
        assert data['email'] == sample_user.email

    def test_delete_user_success(self, client, sample_user):
        """Test successful user deletion"""
        response = client.delete(f'/api/users/{sample_user.id}')
        assert response.status_code == 204

        # Verify user is deleted
        response = client.get(f'/api/users/{sample_user.id}')
        assert response.status_code == 404