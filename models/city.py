#!/usr/bin/python3
"""
Defines the City class that inherits from BaseModel.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    City class for managing city-related data.

    Attributes:
        state_id (str): The ID of the state the city belongs to.
        name (str): The name of the city.
    """

    # Initialize the state_id attribute as an empty string
    state_id = ""
    # Initialize the name attribute as an empty string
    name = ""
