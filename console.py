#!/usr/bin/env python3
""" define a HBNB class """


import cmd


class HBNBCommand(cmd.Cmd):
    """ does various HBNB commands """
    prompt = "(hbnb) "

    def do_create(self, line):
        """ creates a new class instance and prints its str rep """
        if not line:
            print("** class name missing **")
            return
        cls = getattr(self, line)
        if cls is None:
            print("** class doesn't exist **")
            return
        new_instance = cls()
        models.storage.save()
        print(new_instance.id)

    def do_show(self, line):
        """ prints the string rep of an instance based on cls name """
        words = line.split()
        if len(words) < 2:
            print("** class name missing **")
            return
        class_name = words[1]
        if class_name not in models.storage.models:
            print("** class doesn't exist **")
            return
        if len(words) < 3:
            print("** instance id missing **")
            return
        id = words[2]
        obj = models.storage.find_by_id(class_name, id)
        if obj is None:
            print("** no instance found **")
            return
        print(obj)

    def do_destroy(self, line):
        """ deletes an instance based on class name and id """
        words = line.split()
        if len(words) < 2:
            print("** class name missing **")
            return
        class_name = words[1]
        if class_name not in models.storage.models:
            print("** class doesn't exist **")
            return
        if len(words) < 3:
            print("** instance id missing **")
            return
        id = words[2]
        new_instance = models.storage.find_by_id(class_name, id)
        if new_instance is None:
            print("** no instance found **")
            return
        models.storage.delete_by_id(class_name, id)

    def do_all(self,line):
        """ prints str rep of all instances """
        if line:
            class_name = line.split()[0]
            if class_name not in models.storage.models:
                print("** class doesn't exist **")
                return
            objs = models.storage.find_all(class_name)
            print([str(obj) for obj in objs()])

    def emptyline(self):
        """ does nothing after pressing ENTER """
        pass

    def do_quit(self, line):
        """ facilitates quitting the console """
        return True

    def do_EOF(self, line):
        """ facilitates exiting the console """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
