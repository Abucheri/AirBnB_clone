#!/usr/bin/python3
"""Unit tests for the Amenity class."""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class."""

    def test_amenity_inherits_from_base_model(self):
        """Test if Amenity inherits from BaseModel."""
        new_amenity = Amenity()
        self.assertIsInstance(new_amenity, BaseModel)


if __name__ == '__main__':
    unittest.main()
