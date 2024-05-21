#!/usr/bin/python3
"""
Defines the Review class that inherits from BaseModel.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class for managing review-related data.

    Attributes:
        place_id (str): The ID of the place being reviewed.
        user_id (str): The ID of the user who wrote the review.
        text (str): The content of the review.
    """

    # Initialize the place_id attribute as an empty string
    place_id = ""
    
    # Initialize the user_id attribute as an empty string
    user_id = ""
    
    # Initialize the text attribute as an empty string
    text = ""
