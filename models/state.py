#!/usr/bin/python3
"""
Defines the State class that inherits from BaseModel.
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    State class for managing state-related data.

    Attributes:
        name (str): The name of the state.
    """

    # Initialize the name attribute as an empty string
    name = ""
