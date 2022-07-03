#!/usr/bin/python3
"""asd asd asd"""

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review


class FileStorage():
    """Serializes instances and deserializes JSON file to instances:"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Create an object key and sets it to the object."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes objects to the JSON file."""
        aux_dictionary = {}

        for items in self.__objects:
            aux_dictionary[items] = self.__objects[items].to_dict()

        with open(self.__file_path, "w", encoding="UTF-8") as f:
            json.dump(aux_dictionary, f)

    def reload(self):
        """Deserializes the JSON file to objects."""

        if os.path.isfile(self.__file_path) is True:
            with open(self.__file_path, "r") as f:
                new_dict = json.load(f)

            for key, value in new_dict.items():
                self.__objects[key] = eval(value["__class__"])(**value)
