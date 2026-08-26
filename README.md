# FastAPI Project

A basic FastAPI application with CRUD operations.

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:
```bash
# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
uvicorn main:app --reload
```

5. Open your browser and go to:
- API docs: http://127.0.0.1:8000/docs
- Alternative docs: http://127.0.0.1:8000/redoc

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Welcome message |
| GET | `/items` | Get all items |
| GET | `/items/{item_id}` | Get item by ID |
| POST | `/items` | Create new item |
| PUT | `/items/{item_id}` | Update item |
| DELETE | `/items/{item_id}` | Delete item |

## Example Request

### Create an item
```bash
curl -X POST "http://127.0.0.1:8000/items" \
  -H "Content-Type: application/json" \
  -d '{"name": "Laptop", "description": "A powerful laptop", "price": 999.99, "is_available": true}'
```

## Testing

This project includes comprehensive pytest tests. See [TESTING.md](TESTING.md) for details.

To run all tests:
```bash
python -m pytest -v
```
