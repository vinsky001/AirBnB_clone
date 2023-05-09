#!/usr/bin/python3
""" define a HBNB class """


import cmd


class HBNBCommand(cmd.Cmd):
    """ does various HBNB commands """
    prompt = "(hbnb) "

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
