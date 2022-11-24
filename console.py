#!/usr/bin/python3
"""Module contains models a command interpreter"""

import cmd
import sys
from models.base_model import BaseModel

NEW_CLASS = {"BaseModel": BaseModel}

class HBNBCommand(cmd.Cmd):
    """Defines the entry point for the command interpreter"""
    prompt = '(hbnb) '
    ruler = '='

    def do_quit(self, line):
        """Exists console"""
        return sys.exit()

    def do_EOF(self, line):
        """Exits console"""
        return True

    def emptyline(self):
        """Do nothing when empty line is passed"""
        pass

    def do_create(self, arg):
        """Creates a new instance of Model"""
        if not arg:
            print("** class name missing **")

        elif arg not in NEW_CLASS:
            print("** class doesn't exist **")

        else:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
