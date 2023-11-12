#!/usr/bin/python3
"""Module for HBNBCommand class, which is the command
interpreter for the AirBnB clone project
"""
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User


def valid_classes(class_name):
    """Check if the given class name is a valid class in the project."""
    valid_classes_list = ["BaseModel", "User"]
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
        args = arg.split()
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
        args = arg.split()
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
                        else:
                            print("** no instance found **")
                else:
                    print("** class doesn't exist **")
            except Exception:
                print("** class doesn't exist **")

    def do_all(self, arg):
        """Print all string representations of instances."""
        args = arg.split()
        obj_list = []
        if not args or valid_classes(args[0]):
            for key, value in storage.all().items():
                obj_list.append(value.__str__())
            print(obj_list)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Update an instance based on the class name and id."""
        args = arg.split()
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
                            if len(args) < 3:
                                print("** attribute name missing **")
                            elif len(args) < 4:
                                print("** value missing **")
                            else:
                                attr_name = args[2]
                                attr_value = args[3]
                                if ((attr_value.startswith('"') and
                                     attr_value.endswith('"')) or
                                    (attr_value.startswith("'") and
                                     attr_value.endswith("'"))):
                                    attr_value = attr_value[1:-1]
                                setattr(obj, attr_name, attr_value)
                                storage.save()
                        else:
                            print("** no instance found **")
                else:
                    print("** class doesn't exist **")
            except Exception:
                print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
