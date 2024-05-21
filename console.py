#!/usr/bin/python3
"""Console, the command interpreter for managing AirBnB objects."""
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.city import City
from models.review import Review
import re


class HBNBCommand(cmd.Cmd):
    """Command line interface for AirBnB objects management."""

    def __init__(self, *args, **kwargs):
        """Initialize variables and start the shell."""
        super().__init__(*args, **kwargs)
        self.prompt = "(hbnb) "
        self.class_names = [
            "BaseModel",
            "User",
            "State",
            "City",
            "Amenity",
            "Place",
            "Review",
        ]
        self.classes = storage.class_dict()
        self.objects = storage.all()
        storage.reload()

    def default(self, line):
        """Handle unrecognized commands."""
        args = line.split('(')
        if len(args) != 2:
            print("** invalid command **")
            return

        command_args = args[1].split(')')[0]
        command_name = args[0].strip()

        if not command_args:
            print("** invalid command **")
            return

        class_name, action = command_name.split('.')

        if class_name not in self.class_names:
            print("** class doesn't exist **")
            return

        instance_id = None
        update_dict = None

        if action == 'show':  # show BaseModel 1234-1234-1234
            instance_id = command_args.strip().strip('"')
            self.do_show(f"{class_name} {instance_id}")

        elif action == 'destroy':  # destroy BaseModel 1234-1234-1234
            instance_id = command_args.strip().strip('"')
            self.do_destroy(f"{class_name} {instance_id}")

        elif action == 'update':  # update BaseModel 1234-1234-1234 {"name": "John"}
            command_args = command_args.split(',', 1)
            if len(command_args) != 2:
                print("** invalid command **")
                return
            instance_id = command_args[0].strip().strip('"')
            update_dict = eval(command_args[1].strip())
            self.do_update(f"{class_name} {instance_id}", update_dict)

        else:
            print("** invalid command **")

    def emptyline(self):
        """Do nothing on empty input line."""
        pass

    def do_EOF(self, line):
        """Exit the program."""
        return True

    def do_quit(self, line):
        """Exit the program."""
        return True

    def do_create(self, line):
        """Create a new instance of a class."""
        args = line.split()  # split the line into a list of arguments
        if not args:  # if there are no arguments
            print("** class name missing **")
            return
        class_name = args[0]  # the first argument is the class name
        # if the class name is not in the list of classes
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        # create a new instance of the class
        new_instance = self.classes[class_name]()
        new_instance.save()  # save the new instance
        print(new_instance.id)  # print the id of the new instance

    def do_show(self, line):
        """Print the string representation of an instance."""
        args = line.split()  # split the line into a list of arguments
        if not args:  # if there are no arguments
            print("** class name missing **")
            return
        # if the class name is not in the list of classes
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(args) == 1:  # if there is only one argument
            print("** instance id missing **")
            return
        else:  # if there are two arguments
            key = "{}.{}".format(args[0], args[1])  # create a key
            if key in storage.all():  # if the key is in the storage
                obj = storage.all()[key]  # get the object from the storage
                print(obj)  # print the object
            else:  # if the key is not in the storage
                print("** no instance found **")

    def do_destroy(self, line):
        """Delete an instance of a class."""
        args = line.split()  # split the line into a list of arguments
        if not args:  # if there are no arguments
            print("** class name missing **")
            return
        # if the class name is not in the list of classes
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(args) == 1:  # if there is only one argument
            print("** instance id missing **")
            return
        else:  # if there are two arguments
            key = "{}.{}".format(args[0], args[1])  # create a key
            if key in self.objects.keys():  # if the key is in the objects
                del self.objects[key]  # delete the object
                storage._FileStorage__objects = self.objects  # update the objects
                storage.save()  # save the storage
            else:  # if the key is not in the objects
                print("** no instance found **")

    def do_count(self, line):
        """Retrieve the number of instances of a class."""
        args = line.split()  # split the line into a list of arguments
        if len(args) == 1:  # if there is only one argument
            class_name = args[0]  # the first argument is the class name
            # if the class name is in the list of classes
            if class_name in self.class_names:
                # count the number of instances
                count = sum(
                    1 for obj in storage.all().values()
                    if isinstance(obj, eval(class_name)))
                print(count)
            else:  # if the class name is not in the list of classes
                print("** class doesn't exist **")
        else:  # if there is not one argument
            print("** invalid command **")

    def parseline(self, line):
        """Parse the line to handle <class name>.all() and <class name>.count()."""
        original_line = line  # save the original line
        line = line.strip()  # remove leading and trailing whitespace
        class_name = None  # initialize class_name
        command = None  # initialize command

        match = re.match(r'^(\w+)\.(all|count)\(\)$', line) # match the line
        if match:  # if there is a match
            class_name = match.group(1)  # get the class name
            command = match.group(2)  # get the command
            # return the command, class name, and original line
            return command, class_name, original_line
        # return the command, class name, and original line
        return cmd.Cmd.parseline(self, original_line)

    def do_all(self, line):
        """Print all string representations of all instances."""
        args = line.split()  # split the line into a list of arguments
        all_instances = []  # initialize a list of all instances

        if not args:  # if there are no arguments
            # iterate through the objects
            for obj_key, obj in storage.all().items():
                # append the object to the list
                all_instances.append(str(obj))
            # if the class name is not in the classes
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        else:
            class_name = args[0]  # get the class name
            # iterate through the objects
            for obj_key, obj in storage.all().items():
                # if the class name matches
                if obj_key.split(".")[0] == class_name:
                    all_instances.append(str(obj))  # append the object
        print(all_instances)

    def do_update(self, line):
        """Update an instance based on the class name and id."""
        args = line.split()  # split the line into a list of arguments
        obj_dict = storage.all()  # get the objects from the storage

        if len(args) == 0:  # if there are no arguments
            print("** class name missing **")
            return False
        # if the class name is not in the classes
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return False
        if len(args) == 1:  # if there is only one argument
            print("** instance id missing **")
            return False
        # if the key is not in the objects
        if "{}.{}".format(args[0], args[1]) not in obj_dict.keys():
            print("** no instance found **")
            return False
        if len(args) == 2:  # if there are only two arguments
            print("** attribute name missing **")
            return False
        if len(args) == 3:  # if there are only three arguments
            try:  # try to evaluate the argument
                # check if the argument is not a dictionary
                type(eval(args[2])) != dict
            except NameError:  # if the argument is a dictionary
                print("** value missing **")
                return False

        if len(args) == 4:  # if there are only four arguments
            obj = obj_dict["{}.{}".format(args[0], args[1])]  # get the object
            # if the key is in the class
            if args[2] in obj.__class__.__dict__.keys():
                # get the type
                val_type = type(obj.__class__.__dict__[args[2]])
                obj.__dict__[args[2]] = val_type(args[3])  # update the object
            else:  # if the key is not in the class
                obj.__dict__[args[2]] = args[3]  # update the object
        elif type(eval(args[2])) == dict:  # if the argument is a dictionary
            obj = obj_dict["{}.{}".format(args[0], args[1])]  # get the object
            # iterate through the dictionary
            for key, value in eval(args[2]).items():
                if key in obj.__class__.__dict__.keys() and type(
                    obj.__class__.__dict__[key]
                ) in {str, int, float}:  # if the key is in the class
                    # get the type
                    val_type = type(obj.__class__.__dict__[key])
                    obj.__dict__[key] = val_type(value)  # update the object
                else:  # if the key is not in the class
                    obj.__dict__[key] = value  # update the object
        storage.save()  # save the storage


if __name__ == "__main__":
    HBNBCommand().cmdloop()
