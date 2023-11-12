#!/usr/bin/python3
"""Module for FileStorage class."""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """Serializes instances to a JSON file and
    deserializes JSON file to instances.

    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        s_objects = {}
        for key, value in FileStorage.__objects.items():
            s_objects[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            f.write(json.dumps(s_objects))

    def reload(self):
        """Deserializes the JSON file to __objects (only if the file exists).
        """
        try:
            with open(FileStorage.__file_path) as f:
                s_dict = json.load(f)
                for key, value in s_dict.items():
                    cls_name = value["__class__"]
                    del value["__class__"]
                    cls = globals()[cls_name]
                    self.new(cls(**value))
        except FileNotFoundError:
            return
