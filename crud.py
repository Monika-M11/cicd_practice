from typing import Optional, List
from sqlalchemy.orm import Session
from models import DBItem

def get_item_from_db(db: Session, item_id: int) -> Optional[DBItem]:
    """Get an item by ID from database"""
    return db.query(DBItem).filter(DBItem.id == item_id).first()

def get_all_items_from_db(db: Session) -> List[DBItem]:
    """Get all items from database"""
    return db.query(DBItem).all()

def create_item_in_db(db: Session, item: dict) -> DBItem:
    """Create a new item in database"""
    db_item = DBItem(**item)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def update_item_in_db(db: Session, item_id: int, item: dict) -> Optional[DBItem]:
    """Update an item in database"""
    db_item = db.query(DBItem).filter(DBItem.id == item_id).first()
    if db_item:
        for key, value in item.items():
            setattr(db_item, key, value)
        db.commit()
        db.refresh(db_item)
    return db_item

def delete_item_in_db(db: Session, item_id: int) -> bool:
    """Delete an item from database"""
    db_item = db.query(DBItem).filter(DBItem.id == item_id).first()
    if db_item:
        db.delete(db_item)
        db.commit()
        return True
    return False
