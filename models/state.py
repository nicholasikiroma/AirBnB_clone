#!/usr/bin/python3
"""
    contains state class to represent a state
"""
from models.base_model import BaseModel


class State(BaseModel):
    """Represent a state.
    Attributes:
        name (str): The name of the state.
    """
    
    name = ""
