#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place
import unittest


class test_Place(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    @classmethod
    def setUpClass(cls):
        """set up for test"""
        cls.obj = Place()
        cls.obj.name = "Apartment"
        cls.obj.city_id = "4534"
        cls.obj.user_id = "543"
        cls.obj.description = "Bright"
        cls.obj.number_rooms = 2
        cls.obj.number_bathrooms = 1
        cls.obj.max_guest = 4
        cls.obj.price_by_night = 150
        cls.obj.latitude = 54353.5435
        cls.obj.longitude = 5436.7657
        cls.obj.amenity_ids = []

    def is_subclass(self):
        """ tests subclass of BaseModel """
        self.assertTrue(issubclass(self.obj.__class__, BaseModel), True)

    def test_city_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)


if __name__ == "__main__":
    unittest.main()
