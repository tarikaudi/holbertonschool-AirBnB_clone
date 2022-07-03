#!/usr/bin/python3
"""test for amenity"""

import models
import unittest
from models.base_model import BaseModel
from datetime import datetime
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """tests"""

    def test_amenity_set(self):
        """test"""
        self.model = Amenity()
        self.model.save()

    def test_amenenity_start(self):
        self.assertTrue(hasattr(self.model, "name"))
        self.assertEqual(self.model.name, "")

        
if __name__ == '__main__':
    unittest.main()
