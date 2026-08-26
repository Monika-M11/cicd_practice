from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI(
    title="My FastAPI Project",
    description="A basic FastAPI application",
    version="1.0.0"
)


# Model for request validation
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    is_available: bool = True

class ItemResponseDTO(BaseModel):
       item: Item
       error: Optional[str] = None

# In-memory storage (for demo purposes)
items_db: dict[int, Item] = {}
item_id_counter = 0


@app.get("/")
def root():
    """Root endpoint"""
    return {"message": "Welcome to FastAPI!"}


@app.get("/items/{item_id}")
def get_item(item_id: int) -> ItemResponseDTO:
    """Get an item by ID"""
    if item_id not in items_db:
        return {"item": None, "error": "Item not found"}
    return {"item":items_db[item_id]}


@app.get("/items")
def get_all_items():
    """Get all items"""
    return items_db


@app.post("/items")
def create_item(item: Item):
    """Create a new item"""
    global item_id_counter
    item_id_counter += 1
    items_db[item_id_counter] = item
    return {"id": item_id_counter, **item.model_dump()}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    """Update an item"""
    if item_id not in items_db:
        return {"error": "Item not found"}
    items_db[item_id] = item
    return {"id": item_id, **item.model_dump()}


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    """Delete an item"""
    if item_id not in items_db:
        return {"error": "Item not found"}
    del items_db[item_id]
    return {"message": "Item deleted successfully"}
