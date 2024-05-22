"""
Unit tests for the Review class.
"""
import unittest
import sys
from unittest.mock import patch
from datetime import datetime
from models.review import Review
from models.base_model import BaseModel
sys.path.append('../')


class TestReview(unittest.TestCase):
    """
    Unit tests for the Review class.
    """

    def test_inheritance(self):
        """
        Test if Review inherits from BaseModel.
        """
        # Create a Review instance
        review_instance = Review()
        # Check if review_instance is an instance of BaseModel
        self.assertIsInstance(review_instance, BaseModel)

    def test_attributes(self):
        """
        Test if Review instance has the expected attributes.
        """
        # Create a Review instance
        review_instance = Review()
        # Check if the instance has 'id' attribute
        self.assertTrue(hasattr(review_instance, "id"))
        # Check if the instance has 'created_at' attribute
        self.assertTrue(hasattr(review_instance, "created_at"))
        # Check if the instance has 'updated_at' attribute
        self.assertTrue(hasattr(review_instance, "updated_at"))
        # Check if the instance has 'place_id' attribute
        self.assertTrue(hasattr(review_instance, "place_id"))
        # Check if the instance has 'user_id' attribute
        self.assertTrue(hasattr(review_instance, "user_id"))
        # Check if the instance has 'text' attribute
        self.assertTrue(hasattr(review_instance, "text"))
        # Check if 'place_id' is an empty string
        self.assertEqual(review_instance.place_id, "")
        # Check if 'user_id' is an empty string
        self.assertEqual(review_instance.user_id, "")
        # Check if 'text' is an empty string
        self.assertEqual(review_instance.text, "")

    def test_id_is_unique(self):
        """
        Test if each Review instance has a unique id.
        """
        # Create two Review instances
        review_instance1 = Review()
        review_instance2 = Review()
        # Check if their ids are not equal
        self.assertNotEqual(review_instance1.id, review_instance2.id)

    def test_dates_are_datetime(self):
        """
        Test if 'created_at' and 'updated_at' are datetime instances.
        """
        # Create a Review instance
        review_instance = Review()
        # Check if 'created_at' is an instance of datetime
        self.assertIsInstance(review_instance.created_at, datetime)
        # Check if 'updated_at' is an instance of datetime
        self.assertIsInstance(review_instance.updated_at, datetime)

    def test_str_representation(self):
        """
        Test the string representation of a Review instance.
        """
        # Create a Review instance
        review_instance = Review()
        # Expected string format
        expected_format = f"[Review] ({review_instance.id}) {review_instance.__dict__}"
        # Check if the string representation matches the expected format
        self.assertEqual(expected_format, review_instance.__str__())

    def test_save(self):
        """
        Test the save method updates 'updated_at'.
        """
        # Create a Review instance
        review_instance = Review()
        # Store the old 'updated_at' value
        old_updated_at = review_instance.updated_at
        # Call the save method
        review_instance.save()
        # Check if 'updated_at' has been updated
        self.assertNotEqual(old_updated_at, review_instance.updated_at)

    @patch('models.review.Review.save')
    def test_save_called(self, mock_save):
        """
        Test if save method is called.
        """
        # Create a Review instance
        review_instance = Review()
        # Call the save method
        review_instance.save()
        # Check if save was called once
        mock_save.assert_called_once()

    def test_to_dict_contains_right_keys(self):
        """
        Test if to_dict method contains the correct keys.
        """
        # Create a Review instance
        review_instance = Review()
        # Check if 'id' is in the dictionary
        self.assertIn("id", review_instance.to_dict())
        # Check if 'created_at' is in the dictionary
        self.assertIn("created_at", review_instance.to_dict())
        # Check if 'updated_at' is in the dictionary
        self.assertIn("updated_at", review_instance.to_dict())

    def test_to_dict_contains_added_attribute(self):
        """
        Test if to_dict method contains added attributes.
        """
        # Create a Review instance
        review_instance = Review()
        # Add a new attribute
        review_instance.new_attribute = "value"
        # Check if 'new_attribute' is in the dictionary
        self.assertIn("new_attribute", review_instance.to_dict())

    def test_to_dict_correct_time_format(self):
        """
        Test if to_dict method has the correct time format.
        """
        # Create a Review instance
        review_instance = Review()
        # Convert to dictionary
        review_dict = review_instance.to_dict()
        # Check if 'created_at' is a string
        self.assertEqual(type(review_dict["created_at"]), str)
        # Check if 'updated_at' is a string
        self.assertEqual(type(review_dict["updated_at"]), str)

    def test_init_from_dict(self):
        """
        Test initialization of a Review instance from a dictionary.
        """
        # Create a dictionary with attributes
        review_dict = {
            "id": "some-id",
            "created_at": "2021-02-11T00:49:50.921259",
            "updated_at": "2021-02-11T00:49:52.921259",
            "place_id": "some-place-id",
            "user_id": "some-user-id",
            "text": "some-text"
        }
        # Initialize Review instance from dictionary
        review_instance = Review(**review_dict)
        # Check if attributes match the dictionary values
        self.assertEqual(review_instance.id, review_dict["id"])
        self.assertEqual(review_instance.place_id, review_dict["place_id"])
        self.assertEqual(review_instance.user_id, review_dict["user_id"])
        self.assertEqual(review_instance.text, review_dict["text"])

    def test_init_from_empty_dict(self):
        """
        Test initialization of a Review instance from an empty dictionary.
        """
        # Initialize Review instance from an empty dictionary
        review_instance = Review(**{})
        # Check if review_instance is an instance of Review
        self.assertIsInstance(review_instance, Review)
        # Check if the instance has 'id' attribute
        self.assertTrue(hasattr(review_instance, "id"))
        # Check if the instance has 'created_at' attribute
        self.assertTrue(hasattr(review_instance, "created_at"))
        # Check if the instance has 'updated_at' attribute
        self.assertTrue(hasattr(review_instance, "updated_at"))
        # Check if the instance has 'place_id' attribute
        self.assertTrue(hasattr(review_instance, "place_id"))
        # Check if the instance has 'user_id' attribute
        self.assertTrue(hasattr(review_instance, "user_id"))
        # Check if the instance has 'text' attribute
        self.assertTrue(hasattr(review_instance, "text"))


if __name__ == '__main__':
    # Run the unit tests
    unittest.main()
