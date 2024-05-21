#!/usr/bin/python3
"""Defines the FileStorage class for handling the storage of objects."""

import json  # Import the json module for JSON operations
import os  # Import the os module for interacting with the operating system
import datetime as time  # Import datetime module with an alias
from models.base_model import BaseModel  # Import the BaseModel class
from models.user import User  # Import the User class
from models.state import State  # Import the State class
from models.city import City  # Import the City class
from models.place import Place  # Import the Place class
from models.review import Review  # Import the Review class
from models.amenity import Amenity  # Import the Amenity class


class FileStorage:
    """
    Serializes instances to a JSON file
    and deserializes JSON file to instances.
    """
    __file_path = "file.json"  # Path to the JSON file
    __objects = {}  # Dictionary to store all objects

    def new(self, obj):
        """Adds an object to the storage."""
        # Construct the key for the object
        key = obj.__class__.__name__ + "." + obj.id
        # Add the object to the storage dictionary
        self.__objects[key] = obj

    def all(self):
        """Returns all objects in the storage."""
        return self.__objects

    def save(self):
        """Serializes __objects to the JSON file."""
        # Create a dictionary to hold the serialized objects
        serialized_objects = {}
        for key, obj in self.__objects.items():
            # Convert each object to a dictionary
            # and add to serialized_objects
            serialized_objects[key] = obj.to_dict()
        # Open the file in write mode and serialize the objects
        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump(serialized_objects, file, indent=2)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        try:
            # Open the file in read mode
            with open(self.__file_path, "r+", encoding="utf-8") as file:
                # Check if the file is empty
                if os.stat(self.__file_path).st_size == 0:
                    return
                # Read the JSON data from the file
                file.seek(0)
                data = json.load(file)
                # Convert the JSON data back to objects
                for key, value in data.items():
                    self.__objects[key] = eval(value["__class__"])(**value)
        except FileNotFoundError:
            # If the file does not exist, do nothing
            pass

    def class_dict(self):
        """Returns a dictionary of class names
        and their corresponding classes."""
        class_dict = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review,
        }
        return class_dict

    def attribute_dict(self):
        """Returns the valid attributes and their types for each class."""
        attribute_dict = {
            "BaseModel": {
                "id": str,
                "created_at": time.datetime,
                "updated_at": time.datetime,
            },
            "User": {
                "email": str,
                "password": str,
                "first_name": str,
                "last_name": str,
            },
            "State": {"name": str},
            "City": {"state_id": str, "name": str},
            "Amenity": {"name": str},
            "Place": {
                "city_id": str,
                "user_id": str,
                "name": str,
                "description": str,
                "number_rooms": int,
                "number_bathrooms": int,
                "max_guest": int,
                "price_by_night": int,
                "latitude": float,
                "longitude": float,
                "amenity_ids": list,
            },
            "Review": {"place_id": str, "user_id": str, "text": str},
        }
        return attribute_dict
