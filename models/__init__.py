"""Module to create unique FileStorage."""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

default_classes = {"BaseModel": BaseModel}

storage = FileStorage()
storage.reload()
