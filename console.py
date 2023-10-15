import cmd
import re
from models import storage
from models.base_model import BaseModel
import json

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    valid_classes = ["BaseModel", "User", "State", "City", "Place", "Amenity", "Review"]

    def emptyline(self):
        pass

    def default(self, arg):
        command_mappings = {
            "all": self.do_all,
            "show": self.do_show,
            "create": self.do_create,
            "destroy": self.do_destroy,
            "update": self.do_update,
            "count": self.do_count
        }

        command_parts = re.split(r'[.()]', arg)
        command_name = command_parts[0]

        if command_name in command_mappings:
            command_func = command_mappings[command_name]
            command_func(arg)
        else:
            print(f"*** Unknown syntax: {arg}")

    def do_quit(self, arg):
        return True

    def do_EOF(self, arg):
        print("")
        return True

    def do_create(self, arg):
        arg_parts = arg.split()
        if not arg_parts:
            print("** class name missing **")
            return

        class_name = arg_parts[0]
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return

        new_instance = BaseModel()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        arg_parts = arg.split()
        if not arg_parts:
            print("** class name missing **")
            return
        if arg_parts[0] not in self.valid_classes:
            print("** class doesn't exist **")
            return
        if len(arg_parts) < 2:
            print("** instance id missing **")
            return

        obj_dict = storage.all()
        key = f"{arg_parts[0]}.{arg_parts[1]}"
        if key not in obj_dict:
            print("** no instance found **")
        else:
            print(obj_dict[key])

    def do_destroy(self, arg):
        arg_parts = arg.split()
        if not arg_parts:
            print("** class name missing **")
            return
        if arg_parts[0] not in self.valid_classes:
            print("** class doesn't exist **")
            return
        if len(arg_parts) < 2:
            print("** instance id missing **")
            return

        obj_dict = storage.all()
        key = f"{arg_parts[0]}.{arg_parts[1]}"
        if key not in obj_dict:
            print("** no instance found **")
        else:
            del obj_dict[key]
            storage.save()

    def do_all(self, arg):
        obj_list = []
        if arg in self.valid_classes:
            obj_dict = storage.all()
            obj_list = [str(obj) for key, obj in obj_dict.items() if key.startswith(arg)]
        elif not arg:
            obj_dict = storage.all()
            obj_list = [str(obj) for obj in obj_dict.values()]
        else:
            print("** class doesn't exist **")

        print(obj_list)

    def do_count(self, arg):
        arg_parts = arg.split()
        if not arg_parts:
            print("** class name missing **")
            return
        if arg_parts[0] not in self.valid_classes:
            print("** class doesn't exist **")
            return

        obj_dict = storage.all()
        count = len([key for key in obj_dict if key.startswith(arg_parts[0])])
        print(count)

    def do_update(self, arg):
        arg_parts = arg.split()
        if len(arg_parts) < 1:
            print("** class name missing **")
            return
        if arg_parts[0] not in self.valid_classes:
            print("** class doesn't exist **")
            return
        if len(arg_parts) < 2:
            print("** instance id missing **")
            return

        obj_dict = storage.all()
        key = f"{arg_parts[0]}.{arg_parts[1]}"
        if key not in obj_dict:
            print("** no instance found **")
            return

        if len(arg_parts) < 3:
            print("** attribute name missing **")
            return

        if len(arg_parts) < 4:
            print("** value missing **")
            return

        obj = obj_dict[key]
        setattr(obj, arg_parts[2], arg_parts[3])
        obj.save()

if __name__ == "__main__":
    HBNBCommand().cmdloop()   
