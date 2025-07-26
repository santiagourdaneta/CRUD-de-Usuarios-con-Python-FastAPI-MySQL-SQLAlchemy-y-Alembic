# tests/test_api_users.py

import sys
import os

# Add the parent directory of 'tests' to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi.testclient import TestClient
from main import app # Assuming your main FastAPI app is in main.py
import pytest
from app.database.session import get_db, create_test_db_engine, drop_test_db, get_test_db
from sqlalchemy.orm import sessionmaker

@pytest.fixture(scope="module") # Use 'function' scope if you want a fresh DB for EACH test function
def test_db_session():
    # Ensure a fresh engine is created for this test run/module
    test_engine = create_test_db_engine()
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)

    def override_get_db():
        db = TestingSessionLocal()
        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db
    yield # Run the tests
    app.dependency_overrides.clear() # Clear overrides after tests in this scope
    drop_test_db(test_engine) # Clean up the test database

def test_create_user_api(test_db_session):
    client = TestClient(app)
    response = client.post(
        "/users/",
        json={
            "name": "Integration Test User",
            "email": "integration@example.com",
            "password": "securepassword",
            "telefono": "1234567890",
            "fecha_nacimiento": "1990-01-01"
        }
    )
    print(response.json()) # <--- Add this line to see the response body
    print(response.status_code) # <--- Add this to explicitly confirm status code

    assert response.status_code == 200 # Keep this assertion