#!/usr/bin/python3
""" console """

import cmd
from datetime import datetime
import models
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import shlex  # for splitting the line along spaces except in double quotes

classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class HBNBCommand(cmd.Cmd):
    """ HBNH console """
    prompt = '(hbnb) '

    def do_EOF(self, arg):
        """Exits console"""
        return True

    def emptyline(self):
        """ overwriting the emptyline method """
        return False

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def _key_value_parser(self, args):
        """creates a dictionary from a list of strings"""
        new_dict = {}
        for arg in args:
            if "=" in arg:
                kvp = arg.split('=', 1)
                key = kvp[0]
                value = kvp[1]
                if value[0] == value[-1] == '"':
                    value = shlex.split(value)[0].replace('_', ' ')
                else:
                    try:
                        value = int(value)
                    except:
                        try:
                            value = float(value)
                        except:
                            continue
                new_dict[key] = value
        return new_dict

    def do_create(self, arg):
        classname = arg[0]
    if classname not in storage.classes():
        print("** class doesn't exist **")
        return False

    params = {}
    for param in arg[1:]:
        key, value = param.split("=", 1)
        key = key.strip()
        value = value.strip()

        if value.startswith('"') and value.endswith('"'):
            value = value[1:-1]
            value = value.replace("\\", "")
            value = value.replace("_", " ")
        elif "." in value:
            value = float(value)
        else:
            try:
                value = int(value)
            except ValueError:
                pass

        params[key] = value

    try:
        obj = storage.create(classname, **params)
        print(obj.id)
        storage.save()
    except Exception as e:
        print(e)
        return False

    return True

    def do_show(self, arg):
        """Prints an instance as a string based on the class and id"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    print(models.storage.all()[key])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, line):
        """Deletes an instance based on the class and id"""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        return
        class_name = args[0]
        if class_name not in models:
            print("** class doesn't exist **")
        return

        if len(args) < 2:
            print("** instance id missing **")
        return
        instance_id = args[1]

        objects = storage.all()
        key = "{}.{}".format(class_name, instance_id)
        if key in objects:
            del objects[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints string representations of instances"""
        args = shlex.split(arg)
        obj_list = []
        if len(args) == 0:
            obj_dict = models.storage.all()
        elif args[0] in classes:
            obj_dict = models.storage.all(classes[args[0]])
        else:
            print("** class doesn't exist **")
            return False
        for key in obj_dict:
            obj_list.append(str(obj_dict[key]))
        print("[", end="")
        print(", ".join(obj_list), end="")
        print("]")

    def do_update(self, arg):
        """Update an instance based on the class name, id, attribute & value"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        return
        class_name = args[0]
        if class_name not in models:
            print("** class doesn't exist **")
        return

        if len(args) < 2:
            print("** instance id missing **")
        return
        instance_id = args[1]

        objects = storage.all()
        key = "{}.{}".format(class_name, instance_id)
        if key in objects:
            if len(args) < 3:
                print("** attribute name missing **")
            return
        attribute_name = args[2]

        if len(args) < 4:
            print("** value missing **")
            return
            attribute_value = args[3]

            instance = objects[key]
            setattr(instance, attribute_name, attribute_value)
            instance.updated_at = datetime.now()
            storage.save()
        else:
            print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
