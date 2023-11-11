#!/usr/bin/python3
"""Module for HBNBCommand class, which is the command
interpreter for the AirBnB clone project
"""
import cmd


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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
