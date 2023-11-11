#!/usr/bin/python3
"""Module containing the BaseModel class."""

import uuid
from datetime import datetime


class BaseModel:
    """BaseModel class for AirBnB project.

    Attributes:
        id (str): The unique identifier for each instance.
        created_at (datetime): The datetime when the instance is created.
        updated_at (datetime): The datetime when the instance is last updated.
    """

    def __init__(self, *args, **kwargs):
        """Initialize a new instance of BaseModel.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        If kwargs is not empty, the instance is created from a dictionary.
        Otherwise, a new instance is created with a unique id and timestamps.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value,
                            "%Y-%m-%dT%H:%M:%S.%f"))
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Return the string representation of the object."""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """Update the updated_at attribute with the current datetime."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return a dictionary representation of the object."""
        obj_dict = dict(self.__dict__)
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        obj_dict['__class__'] = self.__class__.__name__
        return obj_dict
