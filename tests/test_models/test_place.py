"""
Unit tests for the Place class.
"""
import unittest
import sys
from unittest.mock import patch
from datetime import datetime
from models.place import Place
from models.base_model import BaseModel
sys.path.append('../')


class TestPlace(unittest.TestCase):
    """
    Unit tests for the Place class.
    """

    def setUp(self):
        """
        Set up test variables.
        """
        self.place_instance = Place()  # Create a new Place instance

    def test_initialization(self):
        """
        Test initialization of place instance.
        """
        # Check if place_instance is an instance of Place
        self.assertIsInstance(self.place_instance, Place)
        # Check if city_id is an empty string
        self.assertIs(self.place_instance.city_id, "")
        # Check if user_id is an empty string
        self.assertIs(self.place_instance.user_id, "")
        # Check if name is an empty string
        self.assertIs(self.place_instance.name, "")
        # Check if description is an empty string
        self.assertIs(self.place_instance.description, "")
        # Check if number_rooms is an integer
        self.assertIsInstance(self.place_instance.number_rooms, int)
        # Check if number_rooms is 0
        self.assertEqual(self.place_instance.number_rooms, 0)
        # Check if number_bathrooms is an integer
        self.assertIsInstance(self.place_instance.number_bathrooms, int)
        # Check if number_bathrooms is 0
        self.assertEqual(self.place_instance.number_bathrooms, 0)
        # Check if max_guest is an integer
        self.assertIsInstance(self.place_instance.max_guest, int)
        # Check if max_guest is 0
        self.assertEqual(self.place_instance.max_guest, 0)
        # Check if price_by_night is an integer
        self.assertIsInstance(self.place_instance.price_by_night, int)
        # Check if price_by_night is 0
        self.assertEqual(self.place_instance.price_by_night, 0)
        # Check if latitude is a float
        self.assertIsInstance(self.place_instance.latitude, float)
        # Check if latitude is 0.0
        self.assertEqual(self.place_instance.latitude, 0.0)
        # Check if longitude is a float
        self.assertIsInstance(self.place_instance.longitude, float)
        # Check if longitude is 0.0
        self.assertEqual(self.place_instance.longitude, 0.0)
        # Check if amenity_ids is a list
        self.assertIsInstance(self.place_instance.amenity_ids, list)
        # Check if amenity_ids is an empty list
        self.assertEqual(self.place_instance.amenity_ids, [])

    def test_attribute_types(self):
        """
        Test attribute types.
        """
        self.place_instance.city_id = "12345"  # Set city_id to a string
        self.place_instance.user_id = "abcde"  # Set user_id to a string
        self.place_instance.name = "Test Place"  # Set name to a string
        # Set description to a string
        self.place_instance.description = "Test description"
        self.place_instance.number_rooms = 1  # Set number_rooms to an integer
        # Set number_bathrooms to an integer
        self.place_instance.number_bathrooms = 2
        self.place_instance.max_guest = 3  # Set max_guest to an integer
        # Set price_by_night to an integer
        self.place_instance.price_by_night = 100
        self.place_instance.latitude = 12.34  # Set latitude to a float
        self.place_instance.longitude = -56.78  # Set longitude to a float
        # Set amenity_ids to a list
        self.place_instance.amenity_ids = ["pool", "wifi"]

        # Check if city_id is a string
        self.assertIsInstance(self.place_instance.city_id, str)
        # Check if user_id is a string
        self.assertIsInstance(self.place_instance.user_id, str)
        # Check if name is a string
        self.assertIsInstance(self.place_instance.name, str)
        # Check if description is a string
        self.assertIsInstance(self.place_instance.description, str)
        # Check if number_rooms is an integer
        self.assertIsInstance(self.place_instance.number_rooms, int)
        # Check if number_bathrooms is an integer
        self.assertIsInstance(self.place_instance.number_bathrooms, int)
        # Check if max_guest is an integer
        self.assertIsInstance(self.place_instance.max_guest, int)
        # Check if price_by_night is an integer
        self.assertIsInstance(self.place_instance.price_by_night, int)
        # Check if latitude is a float
        self.assertIsInstance(self.place_instance.latitude, float)
        # Check if longitude is a float
        self.assertIsInstance(self.place_instance.longitude, float)
        # Check if amenity_ids is a list
        self.assertIsInstance(self.place_instance.amenity_ids, list)

    def test_modify_attributes(self):
        """
        Test modification of attributes.
        """
        self.place_instance.city_id = "12345"  # Modify city_id
        self.place_instance.user_id = "abcde"  # Modify user_id
        self.place_instance.name = "Test Place"  # Modify name
        # Modify description
        self.place_instance.description = "Some new description"
        self.place_instance.number_rooms = 5  # Modify number_rooms
        self.place_instance.number_bathrooms = 3  # Modify number_bathrooms
        self.place_instance.max_guest = 7  # Modify max_guest
        self.place_instance.price_by_night = 300  # Modify price_by_night
        self.place_instance.latitude = 33.33  # Modify latitude
        self.place_instance.longitude = -44.44  # Modify longitude
        self.place_instance.amenity_ids = ["sauna"]  # Modify amenity_ids

        # Check if city_id is modified correctly
        self.assertEqual(self.place_instance.city_id, "12345")
        # Check if user_id is modified correctly
        self.assertEqual(self.place_instance.user_id, "abcde")
        # Check if name is modified correctly
        self.assertEqual(self.place_instance.name, "Test Place")
        # Check if description is modified correctly
        self.assertEqual(self.place_instance.description,
                         "Some new description")
        # Check if number_rooms is modified correctly
        self.assertEqual(self.place_instance.number_rooms, 5)
        # Check if number_bathrooms is modified correctly
        self.assertEqual(self.place_instance.number_bathrooms, 3)
        # Check if max_guest is modified correctly
        self.assertEqual(self.place_instance.max_guest, 7)
        # Check if price_by_night is modified correctly
        self.assertEqual(self.place_instance.price_by_night, 300)
        # Check if latitude is modified correctly
        self.assertEqual(self.place_instance.latitude, 33.33)
        # Check if longitude is modified correctly
        self.assertEqual(self.place_instance.longitude, -44.44)
        # Check if amenity_ids is modified correctly
        self.assertEqual(self.place_instance.amenity_ids, ["sauna"])


if __name__ == '__main__':
    unittest.main()  # Run the unit tests
