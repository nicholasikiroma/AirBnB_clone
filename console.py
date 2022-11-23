#!/usr/bin/python3
"""Module contains models a command interpreter"""

import cmd
import sys


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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
