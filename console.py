#!/usr/bin/python3
"""Module contains models a command interpreter"""

import cmd
import sys
import models


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

        elif arg not in models.default_classes:
            print("** class doesn't exist **")

        else:
            new_instance = models.default_classes[arg]
            new_instance = new_instance()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, line):
        """Prints the string representation of an instance
           Args:
                line: CLI arguments
        """
        arg = line.split(' ')

        if line:

            if arg[0] in models.default_classes:
                if len(arg) > 1:
                    key = f"{arg[0]}.{arg[1]}"
                    try:
                        print(models.storage.all()[key])
                    except:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_destroy(self, line):
        """ Deletes an instance based on the class name and id
           Args:
                line: CLI arguments
        """
        arg = line.split(' ')

        if line:

            if arg[0] in models.default_classes:
                if len(arg) > 1:
                    key = f"{arg[0]}.{arg[1]}"
                    try:
                        models.storage.all().pop(key)
                        models.storage.save()
                    except:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_all(self, line):
        """Prints all string representation of all instances"""
        all_obj = []
        if line:
            arg = line.split()
            if arg[0] in models.default_classes:
                for key, instance in models.storage.all().items():
                    if key.split('.')[0] == arg[0]:
                        all_obj.append(str(instance))

            else:
                print("** class doesn't exist **")

        else:
            for key, instance in models.storage.all().items():
                all_obj.append(str(instance))
        if all_obj:
            print(all_obj)

    def do_update(self, line):
        """Updates an instance based on the class name and id"""

        arg = line.split()

        if line:

            if arg[0] in models.default_classes:
                if len(arg) > 1:

                    if len(arg) > 2:

                        if len(arg) > 3:

                            key = f"{arg[0]}.{arg[1]}"
                            try:
                                setattr(models.storage.all()[key],
                                        arg[2], arg[3].strip('"'))
                                models.storage.save()
                            except:
                                print("** no instance found **")
                        else:
                            print("** value missing **")
                    else:
                        print("** attribute name missing **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

            
if __name__ == '__main__':
    HBNBCommand().cmdloop()
