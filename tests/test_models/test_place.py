#!/usr/bin/python3
"""Unit tests for the Place class."""
import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """Test cases for the Place class."""

    def test_place_inherits_from_base_model(self):
        """Test if Place inherits from BaseModel."""
        new_place = Place()
        self.assertIsInstance(new_place, BaseModel)


if __name__ == '__main__':
    unittest.main()
