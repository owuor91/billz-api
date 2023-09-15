from sqlalchemy import (
    Column,
    String,
    Float,
    Enum,
    Date,
    ForeignKey,
    Boolean,
    UniqueConstraint)
from sqlalchemy.dialects.postgresql import UUID
import uuid
from app.base.models import BaseModel
from app.enums import FrequencyEnum


class Bill(BaseModel):
    __tablename__ = "bill"
    bill_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(50), nullable=False)
    amount = Column(Float, nullable=False)
    frequency = Column(Enum(FrequencyEnum), nullable=False)
    due_date = Column(String, nullable=False)
    user_id = Column(UUID(as_uuid=True), ForeignKey("user.user_id"))
    __table_args__ = (UniqueConstraint("name", "user_id",
                                       name="unq_user_bill"),)


class UpcomingBill(BaseModel):
    __tablename__ = "upcoming_bill"
    upcoming_bill_id = Column(UUID(as_uuid=True), primary_key=True,
                              default=uuid.uuid4)
    bill_id = Column(UUID(as_uuid=True), ForeignKey("bill.bill_id"))
    name = Column(String(50), nullable=False)
    amount = Column(Float, nullable=False)
    frequency = Column(Enum(FrequencyEnum), nullable=False)
    due_date = Column(Date, nullable=False)
    user_id = Column(UUID(as_uuid=True), ForeignKey("user.user_id"),
                     nullable=False)
    paid = Column(Boolean, nullable=False)
    __table_args__ = (UniqueConstraint("bill_id", "due_date",
                                      name="unq_upcoming"),)
