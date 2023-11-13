#!/usr/bin/python3
"""Unit tests for the City class."""
import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Test cases for the City class."""

    def test_city_inherits_from_base_model(self):
        """Test if City inherits from BaseModel."""
        new_city = City()
        self.assertIsInstance(new_city, BaseModel)


if __name__ == '__main__':
    unittest.main()
