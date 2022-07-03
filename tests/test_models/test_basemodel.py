#!/usr/bin/python3
"""unitttest basemodel"""

import unittest
import models
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """test basemodel"""
    
    def test_basemodel(self):
        """test for basemodel"""

        base1 = BaseModel()
        base2 = BaseModel()
        self.assertNotEqual(base1.id, base2.id)
        self.assertNotEqual(base1.created_at, base2.created_at)
        self.assertNotEqual(base1.updated_at, base2.updated_at)

    def moer_base(self):
        """more test"""

        base1 = BaseModel()
        base1.name = "Hi"
        base1.save()
        self.assertEqual(base1.name, "Hi")
        self.assertIn(base1, models.storage.all().values())
        self.assertEqual(datetime, type(base1.created_at))
        self.assertEqual(datetime, type(base1.updated_at))
