# test_app.py
import pytest
from app import app as flask_app # Import the app instance

@pytest.fixture
def app():
    yield flask_app

@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()

def test_home_page(client):
    """Test the home page returns a successful response and expected content."""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello, World! CI/CD is cool!" in response.data