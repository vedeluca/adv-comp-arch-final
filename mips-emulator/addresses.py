class AddressHandler:
    def __init__(self):
        self._addresses = dict()

    def set(self, label, position):
        self._addresses[label] = position

    def get(self, label):
        return self._addresses[label]

    def print(self):
        address_string = ""
        for label, position in self._addresses.items():
            position_hex = hex(position)
            address_string += f'{label} {position_hex}\n'
        return address_string
