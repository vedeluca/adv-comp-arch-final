class RegisterHandler:
    def __init__(self):
        self.zero = Register()
        self.one = Register()
        self.two = Register()
        self.three = Register()

    def set(self, name, value):
        if name == "$1":
            self.one.set(value)
        elif name == "$2":
            self.two.set(value)
        elif name == "$3":
            self.three.set(value)
        else:
            raise ValueError(name)

    def get(self, name):
        if name == "$1":
            return self.one.get()
        elif name == "$2":
            return self.two.get()
        elif name == "$3":
            return self.three.get()
        else:
            raise ValueError(name)


class Register:
    def __init__(self, value=0):
        self.value = value

    def set(self, value):
        self.value = value

    def get(self):
        return self.value
