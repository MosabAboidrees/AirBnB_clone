"""
Unit tests for the State class.
"""
import unittest
import sys
from unittest.mock import patch
from models.base_model import BaseModel
from models.state import State
from datetime import datetime
sys.path.append('../')


class TestState(unittest.TestCase):
    """
    Unit tests for the State class.
    """

    def test_state_inheritance(self):
        """
        Test if State inherits from BaseModel.
        """
        # Check if State is a subclass of BaseModel
        self.assertTrue(issubclass(State, BaseModel))

    def test_state_attributes(self):
        """
        Test if State instance has the expected attributes.
        """
        # Create a State instance
        state_instance = State()
        # Check if the instance has 'id' attribute
        self.assertTrue(hasattr(state_instance, "id"))
        # Check if the instance has 'created_at' attribute
        self.assertTrue(hasattr(state_instance, "created_at"))
        # Check if the instance has 'updated_at' attribute
        self.assertTrue(hasattr(state_instance, "updated_at"))
        # Check if the instance has 'name' attribute
        self.assertTrue(hasattr(state_instance, "name"))
        # Check if 'name' is an empty string
        self.assertEqual(state_instance.name, "")

    def test_state_attribute_type(self):
        """
        Test if State instance attributes have the correct types.
        """
        # Create a State instance
        state_instance = State()
        # Check if 'id' is an instance of str
        self.assertIsInstance(state_instance.id, str)
        # Check if 'created_at' is an instance of datetime
        self.assertIsInstance(state_instance.created_at, datetime)
        # Check if 'updated_at' is an instance of datetime
        self.assertIsInstance(state_instance.updated_at, datetime)
        # Check if 'name' is an instance of str
        self.assertIsInstance(state_instance.name, str)

    @patch('models.state.BaseModel.save')
    def test_state_save(self, mock_save):
        """
        Test if the save method is called.
        """
        # Create a State instance
        state_instance = State()
        # Call the save method
        state_instance.save()
        # Check if the save method was called once
        mock_save.assert_called_once()

    @patch('models.state.BaseModel.to_dict')
    def test_state_to_dict(self, mock_to_dict):
        """
        Test if the to_dict method is called.
        """
        # Create a State instance
        state_instance = State()
        # Call the to_dict method
        state_instance.to_dict()
        # Check if the to_dict method was called once
        mock_to_dict.assert_called_once()

    def test_state_init_no_args(self):
        """
        Test if a State instance can be created with no arguments.
        """
        # Create a State instance
        state_instance = State()
        # Check if state_instance is an instance of State
        self.assertIsInstance(state_instance, State)

    def test_state_init_kwargs(self):
        """
        Test if a State instance can be created with keyword arguments.
        """
        # Create a dictionary with attributes
        kwargs = {
            "id": "1234",
            "created_at": datetime.utcnow().isoformat(),
            "updated_at": datetime.utcnow().isoformat(),
            "name": "California"
        }
        # Initialize State instance from dictionary
        state_instance = State(**kwargs)
        # Check if attributes match the dictionary values
        for key, value in kwargs.items():
            if key in ["created_at", "updated_at"]:
                value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
            self.assertEqual(getattr(state_instance, key), value)

    def test_state_str(self):
        """
        Test the string representation of a State instance.
        """
        # Create a State instance
        state_instance = State()
        # Expected string format
        expected_format = f"[State] ({state_instance.id}) {state_instance.__dict__}"
        # Check if the string representation matches the expected format
        self.assertEqual(str(state_instance), expected_format)


if __name__ == "__main__":
    # Run the unit tests
    unittest.main()
