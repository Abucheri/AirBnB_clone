#!/usr/bin/python3
"""Unit tests for the State class."""
import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Test cases for the State class."""

    def test_state_inherits_from_base_model(self):
        """Test if State inherits from BaseModel."""
        new_state = State()
        self.assertIsInstance(new_state, BaseModel)


if __name__ == '__main__':
    unittest.main()
