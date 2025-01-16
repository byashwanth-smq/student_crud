from flask import Blueprint, jsonify, request
from app.services.user_service import UserService
from app.models.user import User, UserUpdate
from sqlalchemy.exc import IntegrityError
from pydantic import ValidationError

bp = Blueprint('users', __name__, url_prefix='/api/users')
user_service = UserService()

@bp.route('/', methods=['POST'])
def create_user():
    try:
        user_data = request.get_json()
        # print('----user---data----', user_data)
        # Validate request data using Pydantic
        # user_data = User(**request.get_json()) #pydantic validation
        # Create user using validated data
        user = user_service.create_user(user_data)
        return jsonify(user.model_dump()), 201
    except ValidationError as e:
        return jsonify({'error': 'Validation error', 'details': e.errors()}), 400
    except IntegrityError:
        return jsonify({'error': 'Username or email already exists'}), 400

@bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    try:
        user = user_service.get_user(user_id)
        return jsonify(user.model_dump())
    except Exception:
        return jsonify({'error': 'User not found'}), 404

@bp.route('/', methods=['GET'])
def get_all_users():
    result = user_service.get_all_users()
    return jsonify(result.model_dump())

@bp.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    try:
        # Validate request data using Pydantic
        user_data = UserUpdate(**request.get_json())
        # Update user using validated data
        user = user_service.update_user(user_id, user_data)
        return jsonify(user.model_dump())
    except ValidationError as e:
        return jsonify({'error': 'Validation error', 'details': e.errors()}), 400
    except IntegrityError:
        return jsonify({'error': 'Username or email already exists'}), 400
    except Exception:
        return jsonify({'error': 'User not found'}), 404

@bp.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        user_service.delete_user(user_id)
        return '', 204
    except Exception:
        return jsonify({'error': 'User not found'}), 404