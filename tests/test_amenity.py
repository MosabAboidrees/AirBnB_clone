import unittest
import sys
from unittest.mock import patch
from models.base_model import BaseModel
from models.amenity import Amenity
from datetime import datetime
sys.path.append('../')


class TestAmenity(unittest.TestCase):
    """
    Unit tests for the Amenity class.
    """

    def test_attribute_defaults(self):
        """
        Test if the default attribute values are correct.
        """
        # Create an instance of the Amenity class
        amenity_instance = Amenity()
        # Check if the default value of 'name' is an empty string
        self.assertEqual(amenity_instance.name, "")

    def test_attribute_assignment(self):
        """
        Test if attributes can be assigned properly.
        """
        # Create an instance of the Amenity class
        amenity_instance = Amenity()
        # Assign a value to 'name'
        amenity_instance.name = "Test Amenity"
        # Check if the value of 'name' is "Test Amenity"
        self.assertEqual(amenity_instance.name, "Test Amenity")

    def test_attributes_exist(self):
        """
        Test if Amenity instance has the expected attributes.
        """
        # Create an instance of the Amenity class
        amenity_instance = Amenity()
        # Check if instance has the attribute 'id'
        self.assertTrue(hasattr(amenity_instance, 'id'))
        # Check if instance has the attribute 'created_at'
        self.assertTrue(hasattr(amenity_instance, 'created_at'))
        # Check if instance has the attribute 'updated_at'
        self.assertTrue(hasattr(amenity_instance, 'updated_at'))
        # Check if instance has the attribute 'name'
        self.assertTrue(hasattr(amenity_instance, 'name'))

    def test_attribute_types(self):
        """
        Test if the attribute types are correct.
        """
        # Create an instance of the Amenity class
        amenity_instance = Amenity()
        # Check if the type of 'id' is a string
        self.assertIsInstance(amenity_instance.id, str)
        # Check if the type of 'created_at' is a datetime object
        self.assertIsInstance(amenity_instance.created_at, datetime)
        # Check if the type of 'updated_at' is a datetime object
        self.assertIsInstance(amenity_instance.updated_at, datetime)
        # Check if the type of 'name' is a string
        self.assertIsInstance(amenity_instance.name, str)


if __name__ == '__main__':
    unittest.main()
