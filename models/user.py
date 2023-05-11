#!/usr/bin/python3
"""
This file inherits from BaseModel
and defines  UserModel class
"""

from models.base_model import BaseModel


class User(BaseModel):
    # User Model

    # class attributes
    email: str = ''
    password: str = ''
    first_name: str = ''
    last_name: str = ''
