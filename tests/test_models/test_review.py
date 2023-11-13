#!/usr/bin/python3
"""Unit tests for the Review class."""
import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Test cases for the Review class."""

    def test_review_inherits_from_base_model(self):
        """Test if Review inherits from BaseModel."""
        new_review = Review()
        self.assertIsInstance(new_review, BaseModel)


if __name__ == '__main__':
    unittest.main()
