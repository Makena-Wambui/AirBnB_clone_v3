#!/usr/bin/python3
"""
User Class from Models Module
"""
import os
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Float
storage_type = os.environ.get('HBNB_TYPE_STORAGE')


class User(BaseModel, Base):
    """User class handles all application users"""
    if storage_type == "db":
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)

        places = relationship('Place', backref='user', cascade='delete')
        reviews = relationship('Review', backref='user', cascade='delete')
    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''

    def __init__(self, *args, **kwargs):
        """initializes user"""
        if "password" in kwargs:
            kwargs["password"] = md5(kwargs["password"].encode()).hexdigest()
        super().__init__(*args, **kwargs)

    @property
    def password(self):
        """ retrieves passwd"""
        return self._password

    @password.setter
    def password(self, value):
        """sets password"""
        self._password = md5(value.encode()).hexdigest()

    def save(self):
        """Updates the updated_at attribute and saves the instance"""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()
