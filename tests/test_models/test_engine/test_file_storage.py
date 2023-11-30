#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
from models.base_model import BaseModel
from models import storage
import os


class test_fileStorage(unittest.TestCase):
    """ Class to test the file storage method """
    if os.getenv("HBNB_TYPE_STORAGE") != "db":
        def setUp(self):
            """ Set up test environment """
        del_list = []
        for key in storage._FileStorage__objects.keys():
            del_list.append(key)
        for key in del_list:
            del storage._FileStorage__objects[key]

        def tearDown(self):
            """ Remove storage file at end of tests """
            try:
                os.remove('file.json')
            except Exception:
                pass

        def test_obj_list_empty(self):
            """ __objects is initially empty """
            self.assertEqual(len(storage.all()), 0)

        def test_new(self):
            """ New object is correctly added to __objects """
            new = BaseModel()
            for obj in storage.all().values():
                temp = obj
            self.assertTrue(temp is obj)

        def test_all(self):
            """ __objects is properly returned """
            new = BaseModel()
            temp = storage.all()
            self.assertIsInstance(temp, dict)

        def test_base_model_instantiation(self):
            """ File is not created on BaseModel save """
            new = BaseModel()
            self.assertFalse(os.path.exists('file.json'))

        def test_empty(self):
            """ Data is saved to file """
            new = BaseModel()
            thing = new.to_dict()
            new.save()
            new2 = BaseModel(**thing)
            self.assertNotEqual(os.path.getsize('file.json'), 0)

        def test_save(self):
            """ FileStorage save method """
            new = BaseModel()
            storage.save()
            self.assertTrue(os.path.exists('file.json'))

        def test_reload(self):
            """ Storage file is successfully loaded to __objects """
            new = BaseModel()
            storage.save()
            storage.reload()
            for obj in storage.all().values():
                loaded = obj
            self.assertEqual(new.to_dict()['id'], loaded.to_dict()['id'])

        def test_reload_empty(self):
            """ Load from an empty file """
            with open('file.json', 'w') as f:
                pass
            with self.assertRaises(ValueError):
                storage.reload()

        def test_reload_from_nonexistent(self):
            """ Nothing happens if file does not exist """
            self.assertEqual(storage.reload(), None)

        def test_base_model_save(self):
            """ BaseModel save method calls storage save """
            new = BaseModel()
            new.save()
            self.assertTrue(os.path.exists('file.json'))

        def test_type_path(self):
            """ Confirm __file_path is string """
            self.assertEqual(type(storage._FileStorage__file_path), str)

        def test_type_objects(self):
            """ Confirm __objects is a dict """
            self.assertEqual(type(storage.all()), dict)

        def test_key_format(self):
            """ Key is properly formatted """
            new = BaseModel()
            _id = new.to_dict()['id']
            for key in storage.all().keys():
                temp = key
            self.assertEqual(temp, 'BaseModel' + '.' + _id)

        def test_storage_var_created(self):
            """ FileStorage object storage created """
            from models.engine.file_storage import FileStorage
            print(type(storage))
            self.assertEqual(type(storage), FileStorage)

    def test_all_with_cls_filter(self):
        """ __objects is filtered by class """
        new1 = BaseModel()
        new2 = User()
        new3 = Place()

        # Filter by BaseModel
        result = storage.all(BaseModel)
        self.assertIn(new1, result.values())
        self.assertNotIn(new2, result.values())
        self.assertNotIn(new3, result.values())

        # Filter by User
        result = storage.all(User)
        self.assertNotIn(new1, result.values())
        self.assertIn(new2, result.values())
        self.assertNotIn(new3, result.values())

        # Filter by Place
        result = storage.all(Place)
        self.assertNotIn(new1, result.values())
        self.assertNotIn(new2, result.values())
        self.assertIn(new3, result.values())

    def test_new_with_cls_filter(self):
        """ new adds object to __objects only if it matches the class filter """
        new1 = BaseModel()
        new2 = User()
        new3 = Place()

        # Add BaseModel object
        storage.new(new1)
        self.assertIn(new1, storage.all().values())

        # Add User object
        storage.new(new2)
        self.assertIn(new2, storage.all(User).values())
        self.assertNotIn(new2, storage.all().values())

        # Add Place object
        storage.new(new3)
        self.assertIn(new3, storage.all(Place).values())
        self.assertNotIn(new3, storage.all().values())

        


if __name__ == "__main__":
    unittest.main()
