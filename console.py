#!/usr/bin/python3
"""Module for HBNBCommand class, which is the command
interpreter for the AirBnB clone project
"""
from datetime import datetime
import cmd
import re
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import shlex


def parse_line(line):
    """Parse the line into a command name and a string containing
    the arguments.
    """
    r_match = re.search(r"\{(.*?)\}", line)
    with_br = re.search(r"\[(.*?)\]", line)
    if r_match is None:
        if with_br is None:
            return [i.strip(",") for i in shlex.split(line)]
        else:
            my_r_match = shlex.split(line[:with_br.span()[0]])
            my_r = [i.strip(",") for i in my_r_match]
            my_r.append(with_br.group())
            return my_r
    else:
        my_r_match = shlex.split(line[:r_match.span()[0]])
        my_r = [i.strip(",") for i in my_r_match]
        my_r.append(r_match.group())
        return my_r


def valid_classes(class_name):
    """Check if the given class name is a valid class in the project."""
    valid_classes_list = ["BaseModel", "User", "State", "City", "Amenity",
                          "Place", "Review"]
    return class_name in valid_classes_list


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class is a command interpreter for managing AirBnB objects.

    Attributes:
        prompt (str): The prompt displayed for each command input.

    Methods:
        emptyline(self): Do nothing on an empty input line.
        do_quit(self, arg): Quit command to exit the program.
        do_EOF(self, arg): Exit the program with EOF (Ctrl+D).
        help_quit(self): Help documentation for the quit command
        help_EOF(self): Help documentation for the EOF command.
    """
    prompt = '(hbnb) '

    def emptyline(self):
        """Do nothing on an empty input line."""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program.

        Args:
            arg (str): Any additional arguments passed (ignored).

        Returns:
            bool: True to exit the program.
        """
        return True

    def do_EOF(self, arg):
        """Exit the program with EOF (Ctrl+D).

        Args:
            arg (str): Any additional arguments passed (ignored).

        Returns:
            bool: True to exit the program.
        """
        return True

    def help_quit(self):
        """Help documentation for the quit command."""
        print("Quit command to exit the program")

    def help_EOF(self):
        """Help documentation for the EOF command."""
        print("Exit the program with EOF (Ctrl+D)")

    def default(self, arg):
        """Handle default behavior for cmd module when an input is invalid."""
        command_mapping = {
                "all": self.do_all,
                "show": self.do_show,
                "destroy": self.do_destroy,
                "count": self.do_count,
                "update": self.do_update
        }
        dot_match = re.search(r"\.", arg)
        if dot_match is not None:
            parts = [arg[:dot_match.span()[0]], arg[dot_match.span()[1]:]]
            parentheses_match = re.search(r"\((.*?)\)", parts[1])
            if parentheses_match is not None:
                sub_command = [parts[1][:parentheses_match.span()[0]],
                               parentheses_match.group()[1:-1]]
                if sub_command[0] in command_mapping.keys():
                    full_command = "{} {}".format(parts[0], sub_command[1])
                    return command_mapping[sub_command[0]](full_command)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_create(self, arg):
        """Create a new instance of HBNB, save it, and print the id."""
        if not arg:
            print("** class name missing **")
        else:
            try:
                if valid_classes(arg):
                    new_instance = eval(arg)()
                    new_instance.save()
                    print(new_instance.id)
                else:
                    print("** class doesn't exist **")
            except Exception:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """Print the string representation of an instance."""
        args = parse_line(arg)
        if not args:
            print("** class name missing **")
        else:
            try:
                class_name = args[0]
                if valid_classes(class_name):
                    if len(args) < 2:
                        print("** instance id missing **")
                    else:
                        instance_id = args[1]
                        key = "{}.{}".format(class_name, instance_id)
                        obj = storage.all().get(key)
                        if obj:
                            print(obj)
                        else:
                            print("** no instance found **")
                else:
                    print("** class doesn't exist **")
            except Exception:
                print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        args = parse_line(arg)
        if not args:
            print("** class name missing **")
        else:
            try:
                class_name = args[0]
                if valid_classes(class_name):
                    if len(args) < 2:
                        print("** instance id missing **")
                    else:
                        instance_id = args[1]
                        key = "{}.{}".format(class_name, instance_id)
                        obj = storage.all().get(key)
                        if obj:
                            del storage.all()[key]
                            storage.save()
                            # print("Instance deleted")
                        else:
                            print("** no instance found **")
                else:
                    print("** class doesn't exist **")
            except Exception:
                print("** class doesn't exist **")

    def do_all(self, arg):
        """Print all string representations of instances."""
        my_arg = parse_line(arg)
        object_list = []
        if not my_arg:
            # Handle the case when no argument is provided
            object_list = [obj.__str__() for obj in storage.all().values()]
        elif valid_classes(my_arg[0]):
            # Handle the case when a valid class is provided
            class_name = my_arg[0]
            class_instance = eval(class_name)
            object_list = [str(obj) for obj in storage.all().values()
                           if isinstance(obj, class_instance)]
        else:
            # Handle the case when an invalid class is provided
            print("** class doesn't exist **")
        print(object_list)

    def do_update(self, arg):
        """Update an instance based on the class name and id."""
        args = parse_line(arg)
        object_dict = storage.all()
        if len(args) == 0:
            print("** class name missing **")
            return False
        if not valid_classes(args[0]):
            print("** class doesn't exist **")
            return False
        if len(args) == 1:
            print("** instance id missing **")
            return False
        instance_key = "{}.{}".format(args[0], args[1])
        if instance_key not in object_dict.keys():
            print("** no instance found **")
            return False
        if len(args) == 2:
            print("** attribute name missing **")
            return False
        if len(args) == 3:
            try:
                type(eval(args[2])) != dict
            except NameError:
                print("** value missing **")
                return False
        if len(args) == 4:
            obj = object_dict[instance_key]
            if args[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[args[2]])
                obj.__dict__[args[2]] = valtype(args[3])
            else:
                obj.__dict__[args[2]] = args[3]
        elif type(eval(args[2])) == dict:
            obj = object_dict[instance_key]
            for key, value in eval(args[2]).items():
                if (key in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[key])
                        in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[key])
                    obj.__dict__[key] = valtype(value)
                else:
                    obj.__dict__[key] = value
        storage.save()

    def do_count(self, arg):
        """Count the number of instances of a class."""
        my_arg = parse_line(arg)
        if not my_arg:
            print("** class name missing **")
        elif not valid_classes(my_arg[0]):
            print("** class doesn't exist **")
        else:
            class_name = my_arg[0]
            class_instance = eval(class_name)
            count = len([obj for obj in storage.all().values()
                        if isinstance(obj, class_instance)])
            print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
