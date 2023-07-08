from sqlalchemy import (
    Column,
    String,
)
from sqlalchemy.dialects.postgresql import UUID
import uuid
from app.base.models import BaseModel


class User(BaseModel):
    __tablename__ = "user"
    user_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    phone_number = Column(String(50), nullable=False, unique=True)
    password = Column(String(256), nullable=False)
