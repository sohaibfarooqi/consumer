import os

from sqlalchemy import Column, DateTime, Integer, String, UniqueConstraint, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    """
    Database table schema for User model.
    For field definition please check `UserSchema`.
    Email address is declared as unique field across
    the table.
    """
    __tablename__ = 'users'
    __table_args__ = (UniqueConstraint('email', name='ux_user_email'),)

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    timestamp = Column(String)
    created_at = Column(DateTime, default=func.now())
    parent_task_id = Column(String)

    def __repr__(self):
        """
        Representaion of User object for easy debugging.
        """
        return "<User(name='%s', email='%s')>" % (self.name, self.email)
