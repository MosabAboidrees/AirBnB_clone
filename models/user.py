#!/usr/bin/python3
"""
Defines the User class for handling user data.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    User class represents a user in the system.

    Attributes:
        email (str): The email of the user.
        password (str): The password of the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
    """

    # Initialize email attribute as an empty string
    email = ""
    # Initialize password attribute as an empty string
    password = ""
    # Initialize first_name attribute as an empty string
    first_name = ""
    # Initialize last_name attribute as an empty string
    last_name = ""
