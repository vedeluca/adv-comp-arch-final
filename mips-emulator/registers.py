class RegisterHandler:
    def __init__(self):
        self._zero = Register("$0")
        self._one = Register("$1")
        self._two = Register("$2")
        self._three = Register("$3")

    def set(self, name, value):
        if name == "$1":
            self._one.set_value(value)
        elif name == "$2":
            self._two.set_value(value)
        elif name == "$3":
            self._three.set_value(value)
        else:
            raise ValueError(name)

    def get(self, name):
        if name == "$0":
            return self._zero
        elif name == "$1":
            return self._one
        elif name == "$2":
            return self._two
        elif name == "$3":
            return self._three
        else:
            raise ValueError(name)

    def print(self):
        zero_print = hex(self._zero.get_value())
        one_print = hex(self._one.get_value())
        two_print = hex(self._two.get_value())
        three_print = hex(self._three.get_value())
        return f'$0 = {zero_print}\n' \
               f'$1 = {one_print}\n' \
               f'$2 = {two_print}\n' \
               f'$3 = {three_print}\n'


class Register:
    def __init__(self, name="$0"):
        self._name = name
        self._value = 0

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

    def get_name(self):
        return self._name