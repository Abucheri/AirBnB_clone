#!/usr/bin/python3
"""Test for the BaseModel class."""

import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Test the initialization of BaseModel."""

    def test_init(self):
        """Test the initialization of BaseModel.

        Assert that a new instance has a non-empty id,
        and created_at and updated_at are instances of datetime.
        """
        new_instance = BaseModel()
        self.assertIsNotNone(new_instance.id)
        self.assertIsInstance(new_instance.created_at, datetime)
        self.assertIsInstance(new_instance.updated_at, datetime)

    def test_str(self):
        """Test the string representation of BaseModel.

        Assert that str method returns the expected formatted string.
        """
        new_instance = BaseModel()
        expected_output = "[BaseModel] ({}) {}".format(new_instance.id,
                                                       new_instance.__dict__)
        self.assertEqual(str(new_instance), expected_output)

    def test_save(self):
        """Test the save method of BaseModel.

        Assert that the updated_at attribute is updated after calling save.
        """
        new_instance = BaseModel()
        old_updated_at = new_instance.updated_at
        new_instance.save()
        self.assertNotEqual(old_updated_at, new_instance.updated_at)

    def test_to_dict(self):
        """Test the to_dict method of BaseModel.

        Assert that the method returns a dictionary with the expected keys
        and values.
        """
        new_instance = BaseModel()
        obj_dict = new_instance.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertEqual(obj_dict['created_at'],
                         new_instance.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'],
                         new_instance.updated_at.isoformat())


if __name__ == '__main__':
    unittest.main()
