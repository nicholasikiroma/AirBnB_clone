"""Module to create unique FileStorage."""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from mosels.user import User

default_classes = {"BaseModel": BaseModel, "User":User}

storage = FileStorage()
storage.reload()
