class AddressHandler:
    def __init__(self):
        self._addresses = list()

    def set(self, label, position):
        address = Address(label, position)
        self._addresses.append(address)

    def get(self, label):
        for address in self._addresses:
            if address.get_label() == label:
                return address.get_position()
        raise ValueError(label)

    def print(self):
        address_string = ""
        for address in self._addresses:
            address_string += f'{address.get_label()} {address.get_position()}\n'
        return address_string


class Address:
    def __init__(self, label, position):
        self._label = label
        self._position = position

    def get_position(self):
        return self._position

    def get_label(self):
        return self._label
