#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.user import User
import unittest


class test_User(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    @classmethod
    def setUpClass(cls):
        """set up for test"""
        cls.obj = User()
        cls.obj.first_name = "Charlie"
        cls.obj.last_name = "Lars"
        cls.obj.email = "test@mail.com"
        cls.obj.password = "GREGE643"

    def is_subclass(self):
        """ tests subclass of BaseModel """
        self.assertTrue(issubclass(self.obj.__class__, BaseModel), True)

    def test_first_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.password), str)


if __name__ == "__main__":
    unittest.main()
