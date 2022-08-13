# Vincent DeLuca
# 8/12/2022
# Advanced Computer Architecture
# Syracuse University

# class containing all the registers
class RegisterHandler:
    def __init__(self):
        self._zero = Register("$0")
        self._one = Register("$1")
        self._two = Register("$2")
        self._three = Register("$3")
        self._four = Register("$4")

    # only $1, $2, and $3 can change their values
    def set(self, name, value):
        if name == "$1":
            self._one.set_value(value)
        elif name == "$2":
            self._two.set_value(value)
        elif name == "$3":
            self._three.set_value(value)
        elif name == "$4":
            self._four.set_value(value)
        else:
            raise ValueError(name)

    # returns the value stored in the register
    def get(self, name):
        if name == "$0":
            return self._zero
        elif name == "$1":
            return self._one
        elif name == "$2":
            return self._two
        elif name == "$3":
            return self._three
        elif name == "$4":
            return self._four
        else:
            raise ValueError(name)

    # returns a string of all the registers and their values
    # each line is a register
    def print(self):
        zero_print = hex(self._zero.get_value())
        one_print = hex(self._one.get_value())
        two_print = hex(self._two.get_value())
        three_print = hex(self._three.get_value())
        four_print = hex(self._four.get_value())
        return f'$0 = {zero_print}\n' \
               f'$1 = {one_print}\n' \
               f'$2 = {two_print}\n' \
               f'$3 = {three_print}\n' \
               f'$4 = {four_print}\n'


# base class for the registers
class Register:
    def __init__(self, name):
        self._name = name
        self._value = 0

    # setter for the value
    def set_value(self, value):
        self._value = value

    # getter for the value
    def get_value(self):
        return self._value

    # returns the name of the register
    def get_name(self):
        return self._name
