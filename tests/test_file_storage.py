#!/usr/bin/python3
"""Unittests for FileStorage class."""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Test cases for FileStorage class."""

    def test_all(self):
        """Test the all() method."""
        storage = FileStorage()
        self.assertEqual(type(storage.all()), dict)

    def test_new(self):
        """Test the new() method."""
        storage = FileStorage()
        obj = BaseModel()
        storage.new(obj)
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.assertIn(key, storage.all())


if __name__ == '__main__':
    unittest.main()
