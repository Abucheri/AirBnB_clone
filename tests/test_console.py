#!/usr/bin/python3
"""Unit tests for the console.py script"""
import unittest
from unittest.mock import patch
from io import StringIO
import os
from console import HBNBCommand
from models import storage


class TestConsole(unittest.TestCase):
    """Test cases for the console.py script"""

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
            HBNBCommand().onecmd("count BaseModel")
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
