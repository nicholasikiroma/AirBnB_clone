#!/usr/bin/python3
"""Module for FileStorage class."""

import json
import models


class FileStorage:
    """class for serialization and deserialization of base classes."""
    __file_path = "file.json"
    __objects = {}

    def __init__(self) -> None:
        """constructor"""
        pass

    def all(self):
        """Returns __objects dict."""

        return self.__objects

    def new(self, obj):
        """Sets new obj in __objects dictionary."""

        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to JSON file."""
        temp = {}
        for obj_id, obj in self.__objects.items():
            temp[obj_id] = obj.to_dict()

        with open(self.__file_path, "w") as json_file:
            json.dump(temp, json_file)

    def reload(self):
        """Deserializes JSON file into __objects."""

        try:

            with open(self.__file_path, "r") as f:
                obj_dict = json.load(f)

            for k, v in obj_dict.items():
                obj_dict_instance = models.default_classes[v["__class__"]](**v)

                self.__objects[k] = obj_dict_instance
        except (FileNotFoundError, IOError):
            pass
