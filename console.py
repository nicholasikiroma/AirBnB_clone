#!/usr/bin/python3
"""Module contains models a command interpreter"""

import cmd
import sys
import models
import re


class HBNBCommand(cmd.Cmd):
    """Defines the entry point for the command interpreter"""
    prompt = '(hbnb) '
    ruler = '='

    def get_command(self, arg):
        """Checks for available commands
            Args:
                arg: name of command
        """
        commands = {"all": HBNBCommand.do_all, "show": HBNBCommand.do_show,
                    "destroy": HBNBCommand.do_destroy,
                    "update": HBNBCommand.do_update}

        if arg in commands:
            return commands[arg]
        else:
            return

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


        if line:
            arg = line.split()

            if arg[0] in models.default_classes:
                if len(arg) > 1:
                    key = f"{arg[0]}.{arg[1]}"
                    try:
                        print(models.storage.all()[key])

                    except KeyError:
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

                    except KeyError:
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
                                setattr(models.storage.all()[key], arg[2], arg[3].strip('"'))
                                models.storage.save()

                            except KeyError:
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


    def default(self, line):
        """
            Handles special commands.

            Usage:
                <class name>.all()
                <class name>.show(<id>)
                <class name>.destroy(<id>)
                <class name>.update(<id>, <attribute name>, <attribute value>)
                <class name>.update(<id>, <dictionary representation>)
        """

        match_pattern = re.fullmatch(r"[A-zA-z]+\.[a-z]+\(.*?\)", line)

        if match_pattern:

            args = line.split('.')
            if args[0] in models.default_classes:

                params = args[1].split("(")
                params[1] = params[1].strip(")")
                items = params[1].split(",")
                items = [arg.strip() for arg in items]

                if len(items) >= 3:
                    temp = items[2]
                    items = [arg.strip('"') for arg in items[:2]]
                    items.append(temp)

                else:
                    items = [arg.strip('"') for arg in items]
                command = self.get_command(params[0])

                if command:
                    valid_args = [arg for arg in items]
                    valid_args.insert(0, args[0])
                    valid_command = " ".join(valid_args)
                    command(self, valid_command)
                else:
                    print("*** Unknown syntax: {}".format(line))
            else:
                print("** class doesn't exist **")
        else:
            print("*** Unknown syntax: {}".format(line))

if __name__ == '__main__':
    HBNBCommand().cmdloop()
