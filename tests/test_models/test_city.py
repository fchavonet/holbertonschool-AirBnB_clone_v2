#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.city import City
import unittest


class test_City(test_basemodel):
    """ Tests for City class """
    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    @classmethod
    def setUpClass(cls):
        """Set up for test"""
        cls.obj = City()
        cls.obj.name = "Toulouse"

    @classmethod
    def tearDown(self):
        """ Removes json file """
        try:
            os.remove("file.json")
        except Exception:
            pass

    def is_subclass(self):
        """ Test subclass of BaseModel """
        self.assertTrue(issubclass(self.obj.__class__, BaseModel), True)

    def test_state_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)


if __name__ == "__main__":
    unittest.main()
