#!/usr/bin/python3
"""Module for FileStorage class."""

import datetime
import json
import os
import models
from models.user import User

class FileStorage:
    """class for serialization and deserialization of base classes."""
    __file_path = "file.json"
    __objects = {}
    
    def all(self):
        """Returns __objects dict."""

        return FileStorage.__objects
        
    def new(self, obj):
        """Sets new obj in __objects dictionary."""

        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj
        
    def save(self):
        """Serializes __objects to JSON file."""
        temp = {}
        for id, obj in FileStorage.__objects.items():
            temp[id] = obj.to_dict()
        
        with open(FileStorage.__file_path, "w") as json_file:
            json.dump(temp, json_file)

       # with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
        #    d = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
         #   json.dump(d, f)
            
    def reload(self):
        """Deserializes JSON file into __objects."""

        if not os.path.isfile(FileStorage.__file_path):
            return

        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            obj_dict = json.load(f)

            for k, v in obj_dict.items():
                obj_dict_instance = models.default_classes[v["__class__"]](**v)

            FileStorage.__objects[k] = obj_dict_instance
