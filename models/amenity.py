#!/usr/bin/python3
"""Defines Amenity class that inherits from BaseModel."""

from models.base_model import BaseModel  # Import the BaseModel class


class Amenity(BaseModel):
    """
    Represents an amenity for the application.
    
    Attributes:
        name (str): The name of the amenity. Default is an empty string.
    """

    name = ""  # Attribute to store the name of the amenity
