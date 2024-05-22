"""
Unit tests for the City class.
"""
import unittest
import sys
from unittest.mock import patch
from datetime import datetime
from models.city import City
from models.base_model import BaseModel

sys.path.append('../')


class TestCity(unittest.TestCase):
    """
    Unit tests for the City class.
    """

    def test_attributes_exist(self):
        """
        Test if City instance has the expected attributes.
        """
        # Create an instance of the City class
        city_instance = City()
        # Check if the instance has the attribute 'id'
        self.assertTrue(hasattr(city_instance, 'id'))
        # Check if the instance has the attribute 'created_at'
        self.assertTrue(hasattr(city_instance, 'created_at'))
        # Check if the instance has the attribute 'updated_at'
        self.assertTrue(hasattr(city_instance, 'updated_at'))
        # Check if the instance has the attribute 'state_id'
        self.assertTrue(hasattr(city_instance, 'state_id'))
        # Check if the instance has the attribute 'name'
        self.assertTrue(hasattr(city_instance, 'name'))

    def test_attribute_types(self):
        """
        Test if the attribute types are correct.
        """
        # Create an instance of the City class
        city_instance = City()
        # Check if the type of the attribute 'id' is a string
        self.assertIsInstance(city_instance.id, str)
        # Check if the type of the attribute 'created_at' is a datetime object
        self.assertIsInstance(city_instance.created_at, datetime)
        # Check if the type of the attribute 'updated_at' is a datetime object
        self.assertIsInstance(city_instance.updated_at, datetime)
        # Check if the type of the attribute 'state_id' is a string
        self.assertIsInstance(city_instance.state_id, str)
        # Check if the type of the attribute 'name' is a string
        self.assertIsInstance(city_instance.name, str)

    def test_attribute_defaults(self):
        """
        Test if the default attribute values are correct.
        """
        # Create an instance of the City class
        city_instance = City()
        # Check if the default value of the attribute 'state_id' is an empty string
        self.assertEqual(city_instance.state_id, "")
        # Check if the default value of the attribute 'name' is an empty string
        self.assertEqual(city_instance.name, "")

    def test_attribute_assignment(self):
        """
        Test if attributes can be assigned properly.
        """
        # Create an instance of the City class
        city_instance = City()
        # Assign a value to the attribute 'state_id'
        city_instance.state_id = "123"
        # Assign a value to the attribute 'name'
        city_instance.name = "Test City"
        # Check if the value of the attribute 'state_id' is correct
        self.assertEqual(city_instance.state_id, "123")
        # Check if the value of the attribute 'name' is correct
        self.assertEqual(city_instance.name, "Test City")


if __name__ == '__main__':
    unittest.main()
