import pytest
from app import create_app, db
from app.models.user import User

@pytest.fixture
def app():
    """Create application for the tests."""
    app = create_app()
    app.config.update({
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': 'postgresql+pg8000://postgres:postgres@localhost:5432/alloydb_test'
    })
    return app

@pytest.fixture
def client(app):
    """Create test client for the tests."""
    return app.test_client()

@pytest.fixture
def runner(app):
    """Create test runner for the tests."""
    return app.test_cli_runner()

@pytest.fixture
def init_database(app):
    """Initialize test database."""
    with app.app_context():
        db.create_all()
        yield db  # this is where the testing happens
        db.session.remove()
        db.drop_all()

@pytest.fixture
def sample_user(init_database):
    """Create a sample user for testing."""
    user = User(username='test_user', email='test@example.com')
    db.session.add(user)
    db.session.commit()
    return user

@pytest.fixture
def mock_db_session(mocker):
    """Mock database session for unit tests."""
    return mocker.patch('app.db.db_handler.db.session')

@pytest.fixture
def auth_headers():
    """Headers for authenticated requests (if needed)."""
    return {
        'Content-Type': 'application/json'
    }