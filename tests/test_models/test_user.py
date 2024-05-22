#!/usr/bin/python3

"""Defines a class TestUser for testing the User module."""

import unittest  # Import the unittest module for creating unit tests
from models.user import User  # Import the User class
from models.base_model import BaseModel  # Import the BaseModel class
import datetime  # Import the datetime module


class TestUser(unittest.TestCase):
    """Defines tests for the User class."""

    @classmethod
    def setUp(cls):
        """Sets up the test case environment for each test."""
        # Create a User instance
        cls.user1 = User()
        # Set the first_name attribute
        cls.user1.first_name = "wad saif"

    @classmethod
    def tearDown(cls):
        """Cleans up after each test."""
        # Delete the User instance
        del cls.user1

    def test_class_exists(self):
        """Tests if the User class exists."""
        # Check if the class type is correct
        result = "<class 'models.user.User'>"
        self.assertEqual(str(type(self.user1)), result)

    def test_inheritance(self):
        """Tests if User is a subclass and instance of BaseModel."""
        # Check if the instance is of type User
        self.assertIsInstance(self.user1, User)
        # Check if the type is exactly User
        self.assertEqual(type(self.user1), User)
        # Check if User is a subclass of BaseModel
        self.assertTrue(issubclass(self.user1.__class__, BaseModel))

    def test_attribute_types(self):
        """Tests if the attribute types are correct."""
        # Check if 'id' attribute is a string
        self.assertIsInstance(self.user1.id, str)
        self.assertEqual(type(self.user1.id), str)
        # Check if 'created_at' attribute is a datetime object
        self.assertIsInstance(self.user1.created_at, datetime.datetime)
        # Check if 'updated_at' attribute is a datetime object
        self.assertIsInstance(self.user1.updated_at, datetime.datetime)
        # Check if 'first_name' attribute is a string
        self.assertIsInstance(self.user1.first_name, str)
        # Check if 'last_name' attribute is a string
        self.assertIsInstance(self.user1.last_name, str)
        # Check if 'email' attribute is a string
        self.assertIsInstance(self.user1.email, str)
        # Check if 'password' attribute is a string
        self.assertIsInstance(self.user1.password, str)

    def test_save_method(self):
        """Tests if the save method updates 'updated_at' correctly."""
        # Save the User instance
        self.user1.save()
        # Check if 'created_at' and 'updated_at' are not the same
        self.assertNotEqual(self.user1.created_at, self.user1.updated_at)

    def test_module_documentation(self):
        """Tests if the User module is documented."""
        # Check if the User class has documentation
        self.assertIsNotNone(User.__doc__)

    def test_has_attributes(self):
        """Tests if the expected attributes exist in the User instance."""
        # Check if 'id' attribute exists
        self.assertTrue(hasattr(self.user1, 'id'))
        # Check if 'created_at' attribute exists
        self.assertTrue(hasattr(self.user1, 'created_at'))
        # Check if 'updated_at' attribute exists
        self.assertTrue(hasattr(self.user1, 'updated_at'))
        # Check if 'first_name' attribute exists
        self.assertTrue(hasattr(self.user1, 'first_name'))
        # Check if 'last_name' attribute exists
        self.assertTrue(hasattr(self.user1, 'last_name'))
        # Check if 'email' attribute exists
        self.assertTrue(hasattr(self.user1, 'email'))
        # Check if 'password' attribute exists
        self.assertTrue(hasattr(self.user1, 'password'))

    def test_to_dict_method(self):
        """Tests if the to_dict method works correctly."""
        # Convert the User instance to a dictionary
        user_dict = self.user1.to_dict()
        # Check if 'created_at' in dictionary is a string
        self.assertEqual(str, type(user_dict['created_at']))
        # Check if 'created_at' matches the isoformat of created_at attribute
        self.assertEqual(user_dict['created_at'],
                         self.user1.created_at.isoformat())
        # Check if 'created_at' attribute is a datetime object
        self.assertEqual(datetime.datetime, type(self.user1.created_at))
        # Check if '__class__' in dictionary matches the class name
        self.assertEqual(user_dict['__class__'], self.user1.__class__.__name__)
        # Check if 'id' in dictionary matches the id attribute
        self.assertEqual(user_dict['id'], self.user1.id)

    def test_unique_id(self):
        """Tests if each instance is created with a unique ID."""
        # Create new User instances
        user2 = User()
        user3 = User()
        user4 = User()
        # Check if the IDs are unique
        self.assertNotEqual(self.user1.id, user2.id)
        self.assertNotEqual(self.user1.id, user3.id)
        self.assertNotEqual(self.user1.id, user4.id)


if __name__ == '__main__':
    unittest.main()
