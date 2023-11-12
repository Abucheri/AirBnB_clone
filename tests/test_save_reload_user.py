#!/usr/bin/python3
"""Module for testing save and reload User instances."""
from models import storage
from models.base_model import BaseModel
from models.user import User
import unittest
import os


class TestSaveReloadUser(unittest.TestCase):
    """Test cases for save and reload of User instances."""

    def tearDown(self):
        """Remove file (file.json) created during the test."""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_save_reload_user(self):
        """Test save and reload of User instances."""
        all_objs = storage.all()
        self.assertIn("BaseModel.2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4",
                      all_objs)
        self.assertIn("BaseModel.a42ee380-c959-450e-ad29-c840a898cfce",
                      all_objs)
        self.assertIn("BaseModel.af9b4cbd-2ce1-4e6e-8259-f578097dd15f",
                      all_objs)
        self.assertIn("BaseModel.38a22b25-ae9c-4fa9-9f94-59b3eb51bfba",
                      all_objs)
        self.assertIn("BaseModel.9bf17966-b092-4996-bd33-26a5353cccb4",
                      all_objs)

        print("-- Reloaded objects --")
        for obj_id in all_objs.keys():
            obj = all_objs[obj_id]
            print(obj)

        print("-- Create a new User --")
        my_user = User()
        my_user.first_name = "Betty"
        my_user.last_name = "Bar"
        my_user.email = "airbnb@mail.com"
        my_user.password = "root"
        my_user.save()
        print(my_user)

        print("-- Create a new User 2 --")
        my_user2 = User()
        my_user2.first_name = "John"
        my_user2.last_name = "Doe"
        my_user2.email = "john.doe@mail.com"
        my_user2.password = "doe"
        my_user2.save()
        print(my_user2)

        self.assertIn("User.{}".format(my_user.id), storage.all())
        self.assertIn("User.{}".format(my_user2.id), storage.all())


if __name__ == "__main__":
    unittest.main()
