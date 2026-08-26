from sqlalchemy import Column, Integer, String, Float, Boolean
from database import Base, engine

# SQLAlchemy Model
class DBItem(Base):
    __tablename__ = "items"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    price = Column(Float, nullable=False)
    is_available = Column(Boolean, nullable=False, default=True)

# Create tables when this module is imported
Base.metadata.create_all(bind=engine)