# /usr/bin/python3
"""Defines the BaseModel class, and the attributes and methods of it"""
import models
import uuid
import datetime


class BaseModel():
    """Defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """Defines the method of creating instances"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)
        else:
            for key in kwargs:
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        value = datetime.datetime.strptime(
                            kwargs[key], "%Y-%m-%dT%H:%M:%S.%f")
                        setattr(self, key, value)
                    else:
                        setattr(self, key, kwargs[key])

    def __str__(self):
        """This methos returns the string representation of an object"""
        return(f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """Saves the current objects into a JSON file"""
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """Converts a BaseModel instance to a standarized format"""
        dictionary = dict(self.__dict__)
        dictionary["__class__"] = self.__class__.__name__
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()

        return dictionary
