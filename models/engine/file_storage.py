#!/usr/bin/python3
"""This is the file storage class for AirBnB"""
import json
from models.base_model import BaseModel
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User


class FileStorage:
    """Serializes instances to a JSON file and deserializes to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        serial_dict = {}
        for key, value in FileStorage.__objects.items():
            serial_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            json.dump(serial_dict, file)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                json_data = json.load(file)
            for key, value in json_data.items():
                cls_name, obj_id = key.split('.')
                obj_dict = value
                obj = eval(cls_name)(**obj_dict)
                FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass


    def close(self):
        """Deserializes the JSON file to objects"""
        self.reload()
