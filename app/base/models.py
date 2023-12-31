import datetime
import logging
from sqlalchemy import Column, DateTime, String, Boolean
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.ext.declarative import declarative_base
from db import db
from app.base.exceptions import DatabaseError
Base = declarative_base()


class BaseModel(Base):

    __abstract__ = True

    date_created = Column(
        DateTime(timezone=True), nullable=False, default=datetime.datetime.now
    )
    date_updated = Column(
        DateTime(timezone=True),
        nullable=False,
        default=datetime.datetime.now,
        onupdate=datetime.datetime.now,
    )
    created_by = Column(String(100), nullable=False)
    updated_by = Column(String(100), nullable=False)
    active = Column(Boolean, nullable=False, default=True)
    meta = Column(JSON, nullable=True, default=dict, server_default="{}")


def save(obj):
    """Commit record to db."""
    session = db.session
    try:
        session.add(obj)
        session.commit()
    except Exception as exc:
        session.rollback()
        logging.exception(exc)
        err = exc.__cause__
        raise DatabaseError(
            f"Problem saving {obj.__class__.__name__} record in database {err}"
        )

    return obj


def get(model, pk=None):
    """
    Get a single record given a pk
    """
    session = db.session
    if pk is not None:
        return session.query(model).get(pk)
    return session.query(model).all()


def get_user_items(model, user_id):
    """
    Get user's records by their user_id
    """
    session = db.session
    result = []
    if user_id is not None:
        result = session.query(model).filter(model.user_id==user_id).all()
    return result

def set_model_dict(obj, model_dict):
    """Set Model Attributes from dict."""
    for k, v in model_dict.items():
        getattr(obj, k, setattr(obj, k, v))
    return obj
