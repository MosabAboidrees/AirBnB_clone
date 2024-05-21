#!/usr/bin/python3
"""Defines the BaseModel class for all other classes in the application."""

import uuid  # Import uuid to generate unique IDs for instances
from datetime import datetime  # Import datetime for timestamp attributes
import models  # Import models to access storage functions


class BaseModel:
    """
    BaseModel serves as the base class for all
    other classes in the application.

    Attributes:
        id (str): A unique identifier for each instance.
        created_at (datetime):
        The datetime when the instance was created.
        updated_at (datetime):
        The datetime when the instance was last updated.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize attributes for the BaseModel instance.
        
        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        if kwargs:
            # If kwargs is provided, set attributes from it
            for key, value in kwargs.items():
                if key in ("created_at", "updated_at"):
                    # Convert string datetime to datetime object
                    setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key != "__class__":
                    # Set other attributes
                    setattr(self, key, value)
        else:
            # If kwargs is not provided, set default attributes
            self.id = str(uuid.uuid4())  # Generate unique ID
            current_time = datetime.now()  # Get the current datetime
            self.created_at = current_time  # Set created_at attribute
            self.updated_at = current_time  # Set updated_at attribute
            models.storage.new(self)  # Register the instance in storage

    def __str__(self):
        """Return string representation of the model object."""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Update the updated_at attribute and save the instance to file storage.
        """
        self.updated_at = datetime.now()  # Update the updated_at timestamp
        models.storage.save()  # Save the instance to storage

    def to_dict(self):
        """
        Generate a dictionary representation of the model object.
        
        Returns:
            dict: A dictionary containing all keys/values of the instance.
        """
        # Copy instance attributes to a new dictionary
        instance_dict = self.__dict__.copy()
        # Add class name to the dictionary
        instance_dict["__class__"] = self.__class__.__name__
        # Convert updated_at to ISO format
        instance_dict["updated_at"] = self.updated_at.isoformat()
        # Convert created_at to ISO format
        instance_dict["created_at"] = self.created_at.isoformat()
        return instance_dict
