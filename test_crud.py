"""
Basic pytest tests for CRUD functions
"""
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base
from models import DBItem
from crud import (
    get_item_from_db, 
    get_all_items_from_db, 
    create_item_in_db, 
    update_item_in_db, 
    delete_item_in_db
)

# Setup test database
TEST_DATABASE_URL = "sqlite:///./test_crud_database.db"

test_engine = create_engine(TEST_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)

# Create test database tables
Base.metadata.create_all(bind=test_engine)

@pytest.fixture
def test_db():
    """Fixture to provide a clean database for each test"""
    # Create all tables
    Base.metadata.create_all(bind=test_engine)
    
    # Create a test session
    db = TestingSessionLocal()
    
    # Yield the database session
    yield db
    
    # Clean up - drop all tables and close the session
    db.close()
    Base.metadata.drop_all(bind=test_engine)

def test_create_item_in_db(test_db):
    """Test creating an item in database"""
    item_data = {
        "name": "Test Item",
        "description": "Test Description",
        "price": 19.99,
        "is_available": True
    }
    
    created_item = create_item_in_db(test_db, item_data)
    
    assert created_item is not None
    assert created_item.id is not None
    assert created_item.name == "Test Item"
    assert created_item.price == 19.99
    assert created_item.is_available == True

def test_get_item_from_db(test_db):
    """Test getting an item from database"""
    # First create an item
    item_data = {
        "name": "Test Item",
        "description": "Test Description",
        "price": 19.99,
        "is_available": True
    }
    
    created_item = create_item_in_db(test_db, item_data)
    
    # Now get the item
    retrieved_item = get_item_from_db(test_db, created_item.id)
    
    assert retrieved_item is not None
    assert retrieved_item.id == created_item.id
    assert retrieved_item.name == "Test Item"

def test_get_nonexistent_item_from_db(test_db):
    """Test getting a non-existent item from database"""
    retrieved_item = get_item_from_db(test_db, 999)
    assert retrieved_item is None

def test_get_all_items_from_db(test_db):
    """Test getting all items from database"""
    # Create some test items
    items_data = [
        {"name": "Item 1", "description": "Desc 1", "price": 10.0, "is_available": True},
        {"name": "Item 2", "description": "Desc 2", "price": 20.0, "is_available": False},
        {"name": "Item 3", "description": "Desc 3", "price": 30.0, "is_available": True},
    ]
    
    for item_data in items_data:
        create_item_in_db(test_db, item_data)
    
    # Get all items
    all_items = get_all_items_from_db(test_db)
    
    assert len(all_items) == 3
    assert all_items[0].name == "Item 1"
    assert all_items[1].name == "Item 2"
    assert all_items[2].name == "Item 3"

def test_update_item_in_db(test_db):
    """Test updating an item in database"""
    # First create an item
    item_data = {
        "name": "Original Name",
        "description": "Original Desc",
        "price": 15.0,
        "is_available": True
    }
    
    created_item = create_item_in_db(test_db, item_data)
    
    # Update data
    update_data = {
        "name": "Updated Name",
        "description": "Updated Desc",
        "price": 25.0,
        "is_available": False
    }
    
    # Update the item
    updated_item = update_item_in_db(test_db, created_item.id, update_data)
    
    assert updated_item is not None
    assert updated_item.name == "Updated Name"
    assert updated_item.price == 25.0
    assert updated_item.is_available == False

def test_update_nonexistent_item_in_db(test_db):
    """Test updating a non-existent item in database"""
    update_data = {
        "name": "Updated Name",
        "description": "Updated Desc",
        "price": 25.0,
        "is_available": False
    }
    
    updated_item = update_item_in_db(test_db, 999, update_data)
    assert updated_item is None

def test_delete_item_in_db(test_db):
    """Test deleting an item from database"""
    # First create an item
    item_data = {
        "name": "Item to Delete",
        "description": "Will be deleted",
        "price": 10.0,
        "is_available": True
    }
    
    created_item = create_item_in_db(test_db, item_data)
    
    # Delete the item
    result = delete_item_in_db(test_db, created_item.id)
    
    assert result == True
    
    # Verify it's deleted
    deleted_item = get_item_from_db(test_db, created_item.id)
    assert deleted_item is None

def test_delete_nonexistent_item_in_db(test_db):
    """Test deleting a non-existent item from database"""
    result = delete_item_in_db(test_db, 999)
    assert result == False

# Clean up after all tests
# Note: This is handled by the test_db fixture for each test
