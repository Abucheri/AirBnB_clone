#!/usr/bin/python3
"""Module for the State class."""
from models.base_model import BaseModel


class State(BaseModel):
    """State class that inherits from BaseModel.

    Attributes:
        name (str): The name of the state.
    """
    name = ""
