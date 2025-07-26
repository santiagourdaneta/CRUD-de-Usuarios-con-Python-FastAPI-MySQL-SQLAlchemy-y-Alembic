import sys
import os
from unittest.mock import Mock

# Add the project root to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from app.crud.user import create_user
from app.schemas.user import UserCreate # Import your Pydantic schema
from app.models.user import User # Import your SQLAlchemy model

def test_create_user_crud():
    mock_db_session = Mock() # Create a mock database session

    # Prepare dummy data - Now include required fields!
    user_data = UserCreate(
        email="test@example.com",
        password="password123",
        name="Test User",
        telefono="0987654321", # Add a valid phone number
        fecha_nacimiento="1985-05-15" # Add a valid date of birth
    )

    # Mock the add, commit, and refresh methods
    mock_db_session.add.return_value = None
    mock_db_session.commit.return_value = None
    mock_db_session.refresh.side_effect = lambda obj: setattr(obj, 'id', 1) # Simulate ID assignment

    # Call the function being tested
    created_user_model = create_user(db=mock_db_session, user=user_data)

    # Assertions
    mock_db_session.add.assert_called_once()
    mock_db_session.commit.assert_called_once()
    mock_db_session.refresh.assert_called_once()

    assert created_user_model.email == user_data.email
    assert created_user_model.id == 1 # Assuming ID is assigned by DB/refresh
    # You might also assert on the hashed_password if you have a real hashing function