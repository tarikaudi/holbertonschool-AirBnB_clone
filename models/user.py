# /usr/bin/python3
"""Contains the class definition for User"""

from models.base_model import BaseModel


class User(BaseModel):
    """Contains the class attribute"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
