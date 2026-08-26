# Testing Guide

This project includes comprehensive pytest tests for the FastAPI application.

## Test Files

### `test_main.py`
Tests for the FastAPI endpoints:
- `test_root_endpoint`: Tests the root endpoint without parameters
- `test_root_endpoint_with_name`: Tests the root endpoint with name parameter
- `test_create_item`: Tests creating a new item via POST /items
- `test_get_item`: Tests getting an item by ID via GET /items/{item_id}
- `test_get_nonexistent_item`: Tests getting a non-existent item
- `test_get_all_items`: Tests getting all items via GET /items
- `test_update_item`: Tests updating an item via PUT /items/{item_id}
- `test_update_nonexistent_item`: Tests updating a non-existent item
- `test_delete_item`: Tests deleting an item via DELETE /items/{item_id}
- `test_delete_nonexistent_item`: Tests deleting a non-existent item

### `test_crud.py`
Tests for the CRUD functions directly:
- `test_create_item_in_db`: Tests the create_item_in_db function
- `test_get_item_from_db`: Tests the get_item_from_db function
- `test_get_nonexistent_item_from_db`: Tests getting a non-existent item from DB
- `test_get_all_items_from_db`: Tests the get_all_items_from_db function
- `test_update_item_in_db`: Tests the update_item_in_db function
- `test_update_nonexistent_item_in_db`: Tests updating a non-existent item in DB
- `test_delete_item_in_db`: Tests the delete_item_in_db function
- `test_delete_nonexistent_item_in_db`: Tests deleting a non-existent item from DB

## Running Tests

### Run all tests
```bash
python -m pytest -v
```

### Run specific test file
```bash
python -m pytest test_main.py -v
python -m pytest test_crud.py -v
```

### Run specific test
```bash
python -m pytest test_main.py::test_create_item -v
python -m pytest test_crud.py::test_get_item_from_db -v
```

## Test Database

The tests use a separate SQLite database (`test_database.db` and `test_crud_database.db`) to avoid interfering with the main application database. These test databases are automatically created and cleaned up for each test.

## Requirements

The following testing dependencies are required:
- `pytest==8.3.2`
- `httpx==0.27.0`

These are included in the `requirements.txt` file.

## Test Structure

Each test uses a fixture (`test_db`) that:
1. Creates a fresh database
2. Provides a database session
3. Cleans up after the test by dropping all tables

This ensures tests are isolated and don't interfere with each other.
