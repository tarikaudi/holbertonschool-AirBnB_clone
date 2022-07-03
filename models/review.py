# /usr/bin/python3
"""Contains the class definition for Review"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Contains the class attribute"""
    place_id = ""
    user_id = ""
    text = ""
