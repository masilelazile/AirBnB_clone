#!/usr/bin/python3
import cmd
import json
import re

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'

    def do_create(self, line):
        """ new instance of BaseModel"""
        if not line:
            print("** class name missing **")
            return
        try:
            # Create an instance of the specified class
            # and save it to the JSON file
            # Print the ID of the created instance
            pass
        except Exception as e:
            print(e)

    def do_show(self, line):
        """ Prints the string representation of an instance based on the class name and id """
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in ["BaseModel", "YourOtherClasses"]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        try:
            # Retrieve and print the instance with the given ID
            pass
        except Exception as e:
            print("** no instance found **")

    def do_destroy(self, line):
         """Deletes an instance based on the class name and id """
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in ["BaseModel", "YourOtherClasses"]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        try:
            pass
        except Exception as e:
            print("** no instance found **")

    def do_all(self, line):
        """ string representations of instances based or not on the class name."""
        args = line.split()
        if args and args[0] not in ["BaseModel", "YourOtherClasses"]:
            print("** class doesn't exist **")
            return
        try:
            if args:
                # Print instances of the specified class
                pass
            else:
                # Print instances of all classes
                pass
        except Exception as e:
            print(e)

    def do_update(self, line):
        """ Updates an instance based on the class name and id by adding and/or updating an attribute """
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in ["BaseModel", "YourOtherClasses"]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        if len(args) < 3:
            print("** attribute name missing **")
            return
        attr_name = args[2]
        if len(args) < 4:
            print("** value missing **")
            return
        attr_value = args[3]

        try:
            # Update the instance with the given ID and attribute
            pass
        except Exception as e:
            print(e)

    def emptyline(self):
        pass

    def do_EOF(self, line):
        print()
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()

