#!/usr/bin/python3
"""Module contains superclass for mananging all Airbnb objects"""
import uuid
import datetime


class BaseModel:
    """Handles initialization, serialization and deserialization of your future instances"""
    def __init__(self):
        """Initialization of class instances"""
        user_id = uuid.uuid4()
        self.id = str(user_id)
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """Override string representation of class instance"""
        return f"[{__class__.__name__}] {self.id} {self.__dict__}"

    def save(self):
        """updates the public instance attribute updated_at with the current datetime"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__"""
        my_dict = {"__class__": __class__.__name__}

        for key in self.__dict__:
            if key in ("created_at", "updated_at"):
                my_dict.update({key: getattr(self, key).isoformat()})
            else:
                my_dict.update({key: getattr(self, key)})

        return my_dict
