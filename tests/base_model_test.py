#!/usr/bin/env python3
""" unittest for base model """


import unittest
from models.base_model import BaseModel
from datetime import datetime
import json


class TestBaseModel(unittest.TestCase):
    """ define unittests for base model """

    def setUp(self):
        """ setup for the proceeding tests """
        self.model = BaseModel()
        self.model.name = "My First Model"
        self.model.my_number = 89

    def test_id_type(self):
        """ test for id type """
        self.assertEqual(type(self.model.id), str)

    def test_created_at_type(self):
        """ test for created at type """
        self.assertEqual(type(self.model.created_at), datetime)

    def test_updated_at_type(self):
        """ test for updated at type """
        self.assertEqual(type(self.model.updated_at), datetime)

    def test_name_type(self):
        """ test for name type """
        self.assertEqual(type(self.model.name), str)

    def test_my_number_type(self):
        """ test for my number type """
        self.assertEqual(type(self.model.my_number), int)

    def test_save_updates_updated_at(self):
        """ test for save updated at """
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(old_updated_at, self.model.updated_at)

    def test_to_dict_returns_dict(self):
        """ test for to dict return type """
        self.assertEqual(type(self.model.to_dict()), dict)

    def test_to_dict_contains_correct_keys(self):
        """ test for dict containing correct keys """
        model_dict = self.model.to_dict()
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)
        self.assertIn('name', model_dict)
        self.assertIn('my_number', model_dict)
        self.assertIn('__class__', model_dict)

    def test_to_dict_created_at_format(self):
        """ test for created at format """
        model_dict = self.model.to_dict()
        created_at = model_dict['created_at']
        self.assertEqual(created_at, self.model.created_at.isoformat())

    def test_to_dict_updated_at_format(self):
        """ test for updated at format """
        model_dict = self.model.to_dict()
        updated_at = model_dict['updated_at']
        self.assertEqual(updated_at, self.model.updated_at.isoformat())


class TestBaseModelTwo(unittest.TestCase):
    """ define unittests for base model two """

    def setUp(self):
        """ setup for proceeding tests two """
        self.my_model = BaseModel()

    def test_id_generation(self):
        """ test for id gen type """
        self.assertIsInstance(self.my_model.id, str)

    def test_str_representation(self):
        """ test for str rep """
        expected = "[BaseModel] ({}) {}".format(
            self.my_model.id, self.my_model.__dict__)
        self.assertEqual(str(self.my_model), expected)

    def test_to_dict_method(self):
        """ test for to dict method """
        my_model_dict = self.my_model.to_dict()
        self.assertIsInstance(my_model_dict['created_at'], str)
        self.assertIsInstance(my_model_dict['updated_at'], str)
        self.assertEqual(my_model_dict['__class__'], 'BaseModel')

    def test_from_dict_method(self):
        """ test for from dict method """
        my_model_dict = self.my_model.to_dict()
        my_new_model = BaseModel(**my_model_dict)
        self.assertIsInstance(my_new_model, BaseModel)
        self.assertEqual(my_new_model.id, self.my_model.id)
        self.assertEqual(my_new_model.created_at, self.my_model.created_at)
        self.assertEqual(my_new_model.updated_at, self.my_model.updated_at)

    def test_created_at_and_updated_at_types(self):
        """ test for created at and updated at types """
        self.assertIsInstance(self.my_model.created_at, datetime)
        self.assertIsInstance(self.my_model.updated_at, datetime)


if __name__ == "__main__":
    unittest.main()
