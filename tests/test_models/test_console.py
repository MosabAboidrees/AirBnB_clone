"""
Unit tests for the HBNBCommand class (console).
"""
import unittest
from unittest.mock import patch, Mock
from io import StringIO
import models
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.city import City
from models.review import Review
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    """
    Unit tests for the HBNBCommand class.
    """

    @classmethod # Run once for the class
    def setUpClass(cls):
        """
        Set up the class-level test environment.
        Creates an instance of HBNBCommand.
        """
        # Create an instance of the command interpreter
        cls.console_instance = HBNBCommand()

    def setUp(self):
        """
        Set up the test environment before each test.
        Resets the storage objects.
        """
        # Reset the storage objects
        storage._FileStorage__objects = {}

    def create_mock_storage(self):
        """
        Create a mock storage object for testing.
        """
        # Create a mock storage object
        mock_storage = Mock()
        # Mock the all method to return an empty dictionary
        mock_storage.all = Mock(return_value={})
        # Mock the save method
        mock_storage.save = Mock()
        # Mock the reload method
        mock_storage.reload = Mock()
        # Return the mock storage object
        return mock_storage

    def test_default_invalid_command(self):
        """
        Test handling of an invalid command.
        """
        # Redirect stdout to capture print output
        with patch('sys.stdout', new=StringIO()) as fake_output:
            # Call the default method with an invalid command
            self.console_instance.default("invalid_command")
            # Check the output
            self.assertEqual(fake_output.getvalue().strip(),
                             "** invalid command **")

    def test_default_invalid_syntax(self):
        """
        Test handling of a command with invalid syntax.
        """
        # Redirect stdout to capture print output
        with patch('sys.stdout', new=StringIO()) as fake_output:
            # Call the default method with invalid syntax
            self.console_instance.default("User.show()")
            # Check the output
            self.assertEqual(fake_output.getvalue().strip(),
                             "** invalid command **")

    def test_default_non_existing_class(self):
        """
        Test handling of a command with a non-existing class.
        """
        # Redirect stdout to capture print output
        with patch('sys.stdout', new=StringIO()) as fake_output:
            # Call the default method with a non-existing class
            self.console_instance.default("NonExistent.show(\"1234\")")
            # Check the output
            self.assertEqual(fake_output.getvalue().strip(),
                             "** class doesn't exist **")

    def test_default_show(self):
        """
        Test the show command.
        """
        # Create a new BaseModel instance
        obj = BaseModel()
        # Save the instance
        obj.save()
        # Redirect stdout to capture print output
        with patch('sys.stdout', new=StringIO()) as fake_output:
            # Call the default method with show command
            self.console_instance.default(f"BaseModel.show(\"{obj.id}\")")
            # Check the output for the instance id
            self.assertIn(obj.id, fake_output.getvalue().strip())

    def test_do_create_no_class(self):
        """
        Test the create command with no class name.
        """
        # Redirect stdout to capture print output
        with patch('sys.stdout', new=StringIO()) as fake_output:
            # Call the create command with no class name
            self.console_instance.do_create("")
            # Check the output
            self.assertEqual(fake_output.getvalue().strip(),
                             "** class name missing **")

    def test_do_create_invalid_class(self):
        """
        Test the create command with an invalid class name.
        """
        # Redirect stdout to capture print output
        with patch('sys.stdout', new=StringIO()) as fake_output:
            # Call the create command with an invalid class name
            self.console_instance.do_create("MyModel")
            # Check the output
            self.assertEqual(fake_output.getvalue().strip(),
                             "** class doesn't exist **")

    def test_do_create_success(self):
        """
        Test the successful creation of a BaseModel instance.
        """
        # Redirect stdout to capture print output
        with patch('sys.stdout', new=StringIO()) as fake_output:
            # Call the create command with BaseModel
            self.console_instance.do_create("BaseModel")
            # Check the output for a valid UUID
            self.assertRegex(fake_output.getvalue().strip(),
                             "^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$")

    def test_do_show_no_class(self):
        """
        Test the show command with no class name.
        """
        # Redirect stdout to capture print output
        with patch('sys.stdout', new=StringIO()) as fake_output:
            # Call the show command with no class name
            self.console_instance.do_show("")
            # Check the output
            self.assertEqual(fake_output.getvalue().strip(),
                             "** class name missing **")

    def test_do_show_no_instance_id(self):
        """
        Test the show command with no instance id.
        """
        # Redirect stdout to capture print output
        with patch('sys.stdout', new=StringIO()) as fake_output:
            # Call the show command with no instance id
            self.console_instance.do_show("User")
            # Check the output
            self.assertEqual(fake_output.getvalue().strip(),
                             "** instance id missing **")

    def test_do_show_nonexistent(self):
        """
        Test the show command with a non-existent instance id.
        """
        # Redirect stdout to capture print output
        with patch('sys.stdout', new=StringIO()) as fake_output:
            # Call the show command with a non-existent instance id
            self.console_instance.do_show(f"BaseModel 12345")
            # Check the output
            self.assertEqual(fake_output.getvalue().strip(),
                             "** no instance found **")

    def test_do_destroy_no_class(self):
        """
        Test the destroy command with no class name.
        """
        # Redirect stdout to capture print output
        with patch('sys.stdout', new=StringIO()) as fake_output:
            # Call the destroy command with no class name
            self.console_instance.do_destroy("")
            # Check the output
            self.assertEqual(fake_output.getvalue().strip(),
                             "** class name missing **")

    def test_do_destroy_no_instance_id(self):
        """
        Test the destroy command with no instance id.
        """
        # Redirect stdout to capture print output
        with patch('sys.stdout', new=StringIO()) as fake_output:
            # Call the destroy command with no instance id
            self.console_instance.do_destroy("User")
            # Check the output
            self.assertEqual(fake_output.getvalue().strip(),
                             "** instance id missing **")

    def test_do_destroy_nonexistent(self):
        """
        Test the destroy command with a non-existent instance id.
        """
        # Redirect stdout to capture print output
        with patch('sys.stdout', new=StringIO()) as fake_output:
            # Call the destroy command with a non-existent instance id
            self.console_instance.do_destroy(f"BaseModel 12345")
            # Check the output
            self.assertEqual(fake_output.getvalue().strip(),
                             "** no instance found **")

    def test_do_count_valid_class(self):
        """
        Test the count command with a valid class name.
        """
        BaseModel()  # Create a new BaseModel instance
        BaseModel()  # Create another BaseModel instance
        # Redirect stdout to capture print output
        with patch('sys.stdout', new=StringIO()) as fake_output:
            # Call the count command with BaseModel
            self.console_instance.do_count("BaseModel")
            # Check the output for the correct count
            self.assertEqual(fake_output.getvalue().strip(), "2")

    def test_do_count_invalid_class(self):
        """
        Test the count command with an invalid class name.
        """
        # Redirect stdout to capture print output
        with patch('sys.stdout', new=StringIO()) as fake_output:
            # Call the count command with an invalid class name
            self.console_instance.do_count("MyModel")
            # Check the output
            self.assertEqual(fake_output.getvalue().strip(),
                             "** class doesn't exist **")

    def test_do_update_no_class(self):
        """
        Test the update command with no class name.
        """
        # Redirect stdout to capture print output
        with patch('sys.stdout', new=StringIO()) as fake_output:
            # Call the update command with no class name
            self.console_instance.do_update("")
            # Check the output
            self.assertEqual(fake_output.getvalue().strip(),
                             "** class name missing **")

    def test_do_update_no_instance_id(self):
        """
        Test the update command with no instance id.
        """
        # Redirect stdout to capture print output
        with patch('sys.stdout', new=StringIO()) as fake_output:
            # Call the update command with no instance id
            self.console_instance.do_update("BaseModel")
            # Check the output
            self.assertEqual(fake_output.getvalue().strip(),
                             "** instance id missing **")

    def test_do_update_no_attribute_name(self):
        """
        Test the update command with no attribute name.
        """
        obj = BaseModel()  # Create a new BaseModel instance
        # Redirect stdout to capture print output
        with patch('sys.stdout', new=StringIO()) as fake_output:
            # Call the update command with no attribute name
            self.console_instance.do_update(f"BaseModel {obj.id}")
            # Check the output
            self.assertEqual(fake_output.getvalue().strip(),
                             "** attribute name missing **")

    def test_do_update_no_value(self):
        """
        Test the update command with no value for the attribute.
        """
        obj = BaseModel()  # Create a new BaseModel instance
        # Redirect stdout to capture print output
        with patch('sys.stdout', new=StringIO()) as fake_output:
            # Call the update command with no value
            self.console_instance.do_update(f"BaseModel {obj.id} name")
            # Check the output
            self.assertEqual(fake_output.getvalue().strip(),
                             "** value missing **")


if __name__ == '__main__':
    unittest.main()  # Run the unit tests
