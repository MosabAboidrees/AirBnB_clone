#!/usr/bin/python3
"""
Unit tests for the BaseModel class.
"""
from unittest.mock import patch
from datetime import datetime
import unittest
import sys
import uuid
from models.base_model import BaseModel

sys.path.append('../')


class TestBaseModel(unittest.TestCase):
    """
    Unit tests for the BaseModel class.
    """

    def setUp(self):
        """
        Set up the test environment before each test.
        Creates a new instance of BaseModel.
        """
        # Create a new instance of BaseModel
        self.base_model_instance = BaseModel()

    def tearDown(self):
        """
        Clean up the test environment after each test.
        Deletes the instance of BaseModel.
        """
        # Delete the instance of BaseModel
        del self.base_model_instance

    def test_init_no_kwargs(self):
        """
        Test initializing a BaseModel instance without kwargs.
        Ensures that the instance has an id, created_at,
        and updated_at attributes.
        """
        # Check if id is not None
        self.assertIsNotNone(self.base_model_instance.id)
        # Check if id is a string
        self.assertTrue(isinstance(self.base_model_instance.id, str))
        # Check if created_at is a datetime object
        self.assertTrue(isinstance(self.base_model_instance.created_at,
                                   datetime))
        # Check if updated_at is a datetime object
        self.assertTrue(isinstance(self.base_model_instance.updated_at,
                                   datetime))
        # Check if created_at and updated_at are the same
        self.assertEqual(self.base_model_instance.created_at,
                         self.base_model_instance.updated_at)

    def test_init_with_kwargs(self):
        """
        Test initializing a BaseModel instance with kwargs.
        Ensures that the instance attributes are set
        correctly from the kwargs.
        """
        # Generate a random id
        test_id = str(uuid.uuid4())
        # Get the current time
        test_time = datetime.now()
        # Create a dictionary of test kwargs
        test_kwargs = {
            'id': test_id,
            'created_at': test_time.isoformat(),
            'updated_at': test_time.isoformat(),
            '__class__': 'SomeClass'
        }
        # Create a new instance of BaseModel with the test kwargs
        base_model_with_kwargs = BaseModel(**test_kwargs)
        # Check if the id is the same as the test id
        self.assertEqual(base_model_with_kwargs.id, test_id)
        # Check if the created_at is the same as the test time
        self.assertEqual(base_model_with_kwargs.created_at, test_time)
        # Check if the updated_at is the same as the test time
        self.assertEqual(base_model_with_kwargs.updated_at, test_time)

    def test_str(self):
        """
        Test the string representation of a BaseModel instance.
        Ensures that the string is in the expected format.
        """
        # Expected string format
        expected_str_format = "[BaseModel] ({}) {}".format(
            self.base_model_instance.id, self.base_model_instance.__dict__)
        # Check if the expected string format is the same
        # as the string representation of the instance
        self.assertEqual(expected_str_format, str(self.base_model_instance))

    @patch('models.storage') # Mock the storage module
    def test_save(self, mock_storage):
        """
        Test the save method of a BaseModel instance.
        Ensures that updated_at is updated and storage.save() is called.
        """
        # Get the previous updated_at
        previous_updated_at = self.base_model_instance.updated_at
        # Call the save method
        self.base_model_instance.save()
        # Check if updated_at is greater than the previous updated_at
        self.assertGreater(self.base_model_instance.updated_at,
                           previous_updated_at)
        # Check if storage.save() was called
        mock_storage.save.assert_called_once()

    def test_to_dict(self):
        """
        Test the to_dict method of a BaseModel instance.
        Ensures that the dictionary contains the correct keys and values.
        """
        # Get the dictionary representation of the instance
        model_dict = self.base_model_instance.to_dict()
        # Expected keys in the dictionary
        expected_keys = {"id", "__class__", "created_at", "updated_at"}
        # Check if the expected keys are in the dictionary
        self.assertTrue(expected_keys.issubset(model_dict.keys()))
        # Check if the __class__ key has the correct value
        self.assertEqual(model_dict["__class__"], "BaseModel")
        # Check if the created_at key has the correct value
        self.assertEqual(model_dict["created_at"],
                         self.base_model_instance.created_at.isoformat())
        # Check if the updated_at key has the correct value
        self.assertEqual(model_dict["updated_at"],
                         self.base_model_instance.updated_at.isoformat())
        # Check if _sa_instance_state is not in the dictionary
        self.assertNotIn("_sa_instance_state", model_dict)

    def test_to_dict_with_extra_attribute(self):
        """
        Test the to_dict method with an extra attribute.
        Ensures that the extra attribute is included in the dictionary.
        """
        # Add an extra attribute to the instance
        self.base_model_instance.name = "Test Name"
        # Get the dictionary representation of the instance
        model_dict = self.base_model_instance.to_dict()
        # Check if the extra attribute is in the dictionary
        self.assertIn("name", model_dict)
        # Check if the extra attribute has the correct value
        self.assertEqual(model_dict["name"], "Test Name")


if __name__ == '__main__':
    unittest.main()
