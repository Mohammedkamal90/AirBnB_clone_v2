#!/usr/bin/python3
import json
import os
from models.base_model import BaseModel

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of all objects"""
        if cls:
            return {k: v for k, v in self.__objects.items() if isinstance(v, cls)}
        return self.__objects

    def new(self, obj):
        """Adds a new object to the dictionary"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to JSON file"""
        save_dict = {k: v.to_dict() for k, v in self.__objects.items()}
        with open(self.__file_path, 'w') as f:
            json.dump(save_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as f:
                loaded_dict = json.load(f)
                self.__objects = {k: BaseModel(**v) for k, v in loaded_dict.items()}
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Deletes obj from __objects if it's inside"""
        if obj is not None:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            if key in self.__objects:
                del self.__objects[key]
                self.save()
