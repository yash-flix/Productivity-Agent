from datetime import datetime

from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import String

from app.database.database import Base


class Todo(Base):

    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)

    task = Column(String, nullable=False, unique=True)

    priority = Column(String, default="Medium")

    completed = Column(Boolean, default=False)

    created_at = Column(DateTime, default=datetime.utcnow)

    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )