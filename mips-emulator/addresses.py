# Vincent DeLuca
# 8/12/2022
# Advanced Computer Architecture
# Syracuse University

# class containing all the addresses
class AddressHandler:
    def __init__(self):
        # addresses kept in a dictionary
        self._addresses = dict()

    # set address based on label
    def set(self, label, position):
        self._addresses[label] = position

    # get position with label
    def get(self, label):
        return self._addresses[label]

    # returns a string with all the address labels and positions
    # each line is an address
    def print(self):
        address_string = ""
        for label, position in self._addresses.items():
            position_hex = hex(position)
            address_string += f'{label} {position_hex}\n'
        return address_string
