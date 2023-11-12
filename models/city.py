#!/usr/bin/python3
"""Module for the City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """City class that inherits from BaseModel.

    Attributes:
        state_id (str): The state id associated with the city.
        name (str): The name of the city.
    """
    state_id = ""
    name = ""
