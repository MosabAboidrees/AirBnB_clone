"""Module for testing FileStorage class"""
import sys
import unittest
from models.engine.file_storage import FileStorage
from unittest.mock import patch, mock_open
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import json
import os
from io import StringIO
sys.path.append('../../')


class TestFileStorage(unittest.TestCase):
    """Tests for the FileStorage class"""

    def setUp(self):
        """Set up test variables"""
        # Create an instance of FileStorage
        self.storage = FileStorage()
        # Clear the objects dictionary
        self.storage._FileStorage__objects = {}
        # Create instances of different models
        self.base_model = BaseModel()
        self.user = User()  # Create a new User instance
        self.state = State()  # Create a new State instance
        self.city = City()  # Create a new City instance
        self.amenity = Amenity()  # Create a new Amenity instance
        self.place = Place()  # Create a new Place instance
        self.review = Review()  # Create a new Review instance

    def test_new(self):
        """Test adding a new object to the storage"""
        # Add base_model to storage
        self.storage.new(self.base_model)
        # Generate the key for the object
        key = "{}.{}".format(self.base_model.__class__.__name__,
                             self.base_model.id)
        # Check if the object is in the storage
        self.assertIn(key, self.storage._FileStorage__objects)

    def test_all(self):
        """Test retrieving all objects from the storage"""
        # Add base_model to storage
        self.storage.new(self.base_model)
        # Retrieve all objects
        all_objects = self.storage.all()
        # Check if the number of objects is correct
        self.assertEqual(len(all_objects), 1)

    @patch("builtins.open", new_callable=mock_open)  # Mock the open function
    @patch("json.dump")  # Mock the json.dump function
    def test_save(self, mock_json_dump, mock_open):
        """Test saving objects to a file"""
        # Add base_model to storage
        self.storage.new(self.base_model)
        # Save the objects to a file
        self.storage.save()
        # Check if open was called with the correct arguments
        mock_open.assert_called_once_with(FileStorage._FileStorage__file_path,
                                          "w", encoding="utf-8")
        # Check if json.dump was called once
        mock_json_dump.assert_called_once()

    @patch("os.stat")  # Mock the os.stat function
    # Mock the open function
    @patch("builtins.open", new_callable=mock_open, read_data="{}")
    def test_reload_empty(self, mock_open, mock_stat):
        """Test reloading from an empty file"""
        # Set the file size to 0
        mock_stat.return_value.st_size = 0
        # Reload the storage
        self.storage.reload()
        # Check if the objects dictionary is empty
        self.assertFalse(self.storage._FileStorage__objects)

        # Mock the open function with data
    @patch("builtins.open", new_callable=mock_open,
           read_data='{"BaseModel.1234": {"__class__": "BaseModel", \
               "id":"1234", "created_at": "2021-11-02T14:15:22", \
                   "updated_at": "2021-11-02T14:15:22"}}')
    def test_reload_with_data(self, mock_open):
        """Test reloading from a file with data"""
        # Reload the storage
        self.storage.reload()
        # Check if the objects dictionary is not empty
        self.assertTrue(self.storage._FileStorage__objects)
        # Generate the key for the object
        key = "BaseModel.1234"
        # Check if the key is in the storage
        self.assertIn(key, self.storage._FileStorage__objects)
        # Retrieve the object
        obj = self.storage._FileStorage__objects[key]
        # Check if the object is an instance of BaseModel
        self.assertIsInstance(obj, BaseModel)
        # Check if the object's id is correct
        self.assertEqual(obj.id, "1234")

    # Mock the open function to raise FileNotFoundError
    @patch("builtins.open", side_effect=FileNotFoundError)
    def test_reload_not_found(self, mock_open):
        """Test reloading when the file is not found"""
        # Reload the storage
        self.storage.reload()
        # Check if open was called with the correct arguments
        mock_open.assert_called_once_with(FileStorage._FileStorage__file_path,
                                          "r+", encoding="utf-8")
        # Check if the objects dictionary is empty
        self.assertFalse(self.storage._FileStorage__objects)

    def test_class_dict(self):
        """Test retrieving the class dictionary"""
        # Retrieve the class dictionary
        classes = self.storage.class_dict()
        # Check if BaseModel is in the class dictionary
        self.assertEqual(classes["BaseModel"], BaseModel)

    def test_attribute_dict(self):
        """Test retrieving the attribute dictionary"""
        # Retrieve the attribute dictionary
        attributes = self.storage.attribute_dict()
        # Check if 'id' is in the attribute dictionary for BaseModel
        self.assertIn("id", attributes["BaseModel"])
        # Check if the type of 'id' is correct
        self.assertEqual(attributes["BaseModel"]["id"], str)

    def tearDown(self):
        """Clean up after each test"""
        # Remove the storage file if it exists
        try:
            os.remove(self.storage._FileStorage__file_path)
        except FileNotFoundError:
            pass


if __name__ == '__main__':
    unittest.main()  # Run the unittests
