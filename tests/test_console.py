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

    def test_non_interactive_help_command(self):
        """Test non-interactive mode with help command"""
        command = "echo 'help' | ./console.py"
        with os.popen(command) as p:
            output = p.read()
            self.assertIn("Documented commands", output)
            self.assertIn("quit", output)


if __name__ == '__main__':
    unittest.main()
