#!/usr/bin/python3
"""Unit tests for the console.py script"""
import unittest
from unittest.mock import patch
from io import StringIO
import os
from console import HBNBCommand
from console import parse_line
from console import valid_classes
from models import storage
import uuid


class TestConsole(unittest.TestCase):
    """Test cases for the console.py script"""

    def test_prompt_displayed(self):
        """Test the prompt displayed for the console."""
        cmd_obj = HBNBCommand()
        self.assertEqual(cmd_obj.prompt, '(hbnb) ')

    def test_emptyline(self):
        """Test emptyline command"""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            cmd_obj = HBNBCommand()
            cmd_obj.onecmd('')
            self.assertEqual(fake_out.getvalue(), '')

    def test_parse_line_with_patch(self):
        """Test the 'parse_line' method correctly parses a line into a command
        name and a string containing the arguments.
        """
        with patch('sys.stdout', new=StringIO()) as fake_out:
            parse_line("show BaseModel {}".format(uuid.uuid4()))
            expected_output = ['show', 'BaseModel', '1234']
            self.assertEqual(parse_line("show BaseModel 1234"),
                             expected_output)

    def test_valid_classes_with_patch_imported(self):
        """The 'valid_classes' method correctly checks if the given class
        name is a valid class in the project.
        """
        with patch('sys.stdout', new=StringIO()) as fake_out:
            result = valid_classes('BaseModel')
            self.assertEqual(result, True)

    def test_do_update_with_valid_id_with_patch_imported_fixed(self):
        """The 'do_update' method updates an instance based on the
        class name and id correctly when a valid id is provided.
        """
        with patch('sys.stdout', new=StringIO()) as fake_out:
            cmd_obj = HBNBCommand()
            cmd_obj.do_create('BaseModel')
            obj_id = fake_out.getvalue().strip()
            cmd_obj.do_update(f'BaseModel {obj_id} name "John Doe"')
            obj = storage.all()['BaseModel.{}'.format(obj_id)]
            self.assertIsNotNone(obj)
            self.assertEqual(obj.name, "John Doe")

    def test_do_EOF_exits_program(self):
        """The 'do_EOF' method exits the program with EOF (Ctrl+D) when
        called.
        """
        with patch('sys.stdout', new=StringIO()) as fake_out:
            cmd_obj = HBNBCommand()
            cmd_obj.onecmd("EOF")
            self.assertEqual(fake_out.getvalue(), '')
            self.assertTrue(cmd_obj.do_EOF(None))

    def test_help_quit(self):
        """The 'help_quit' method prints help documentation
        for the quit command.
        """
        cmd_obj = HBNBCommand()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            cmd_obj.help_quit()
            self.assertEqual(fake_out.getvalue(),
                             "Quit command to exit the program\n")

    def test_help_EOF_fixed(self):
        """The 'help_EOF' method prints help documentation
        for the EOF command.
        """
        cmd_obj = HBNBCommand()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            cmd_obj.help_EOF()
            self.assertEqual(fake_out.getvalue(),
                             "Exit the program with EOF (Ctrl+D)\n")

    def test_quit_command(self):
        """Test the quit command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(HBNBCommand().onecmd("quit"))
            self.assertEqual(f.getvalue(), "")

    def test_EOF_command(self):
        """Test the EOF command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(HBNBCommand().onecmd("EOF"))
            self.assertEqual(f.getvalue(), "")

    def test_help_command(self):
        """Test the help command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
            output = f.getvalue()
            self.assertIn("Documented commands", output)
            self.assertIn("quit", output)

    def test_create_command(self):
        """Test the create command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            output = f.getvalue()
            self.assertTrue(output.strip().isdigit())

    def test_show_command(self):
        """Test the show command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
            HBNBCommand().onecmd(f"show BaseModel {obj_id}")
            output = f.getvalue()
            self.assertIn(obj_id, output)

    def test_destroy_command(self):
        """Test the destroy command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
            HBNBCommand().onecmd(f"destroy BaseModel {obj_id}")
            self.assertNotIn(obj_id, storage.all())

    def test_all_command(self):
        """Test the all command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            HBNBCommand().onecmd("create User")
            HBNBCommand().onecmd("all")
            output = f.getvalue()
            self.assertIn("BaseModel", output)
            self.assertIn("User", output)

    def test_update_command(self):
        """Test the update command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
            HBNBCommand().onecmd(f"update BaseModel {obj_id} name 'new_name'")
            updated_obj = storage.all()[f"BaseModel.{obj_id}"]
            self.assertEqual(updated_obj.name, "new_name")

    def test_count_command(self):
        """Test the count command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            HBNBCommand().onecmd("create BaseModel")
            HBNBCommand().onecmd("BaseModel.count()")
            output = f.getvalue()
            self.assertEqual(output.strip(), "2")

    def test_non_interactive_help_command(self):
        """Test non-interactive mode with help command"""
        command = "echo 'help' | ./console.py"
        with os.popen(command) as p:
            output = p.read()
            self.assertIn("Documented commands", output)
            self.assertIn("quit", output)

    def test_non_interactive_create_command(self):
        """Test non-interactive mode with create command"""
        command = "echo 'create BaseModel' | ./console.py"
        with os.popen(command) as p:
            output = p.read().strip()
            self.assertTrue(output.isdigit())

    def test_non_interactive_destroy_command(self):
        """Test non-interactive mode with destroy command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
            command = f"echo 'destroy BaseModel {obj_id}' | ./console.py"
            with os.popen(command) as p:
                output = p.read()
                self.assertNotIn(obj_id, storage.all())

    def test_non_interactive_all_command(self):
        """Test non-interactive mode with all command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            HBNBCommand().onecmd("create User")
            command = "echo 'all' | ./console.py"
            with os.popen(command) as p:
                output = p.read()
                self.assertIn("BaseModel", output)
                self.assertIn("User", output)

    def test_non_interactive_update_command(self):
        """Test non-interactive mode with update command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
            command = f"echo 'update BaseModel {obj_id} name new_name' \
                    | ./console.py"
            with os.popen(command) as p:
                updated_obj = storage.all()[f"BaseModel.{obj_id}"]
                self.assertEqual(updated_obj.name, "new_name")

    def test_non_interactive_count_command(self):
        """Test non-interactive mode with count command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            HBNBCommand().onecmd("create BaseModel")
            command = "echo 'count BaseModel' | ./console.py"
            with os.popen(command) as p:
                output = p.read().strip()
                self.assertEqual(output, "2")


if __name__ == '__main__':
    unittest.main()
