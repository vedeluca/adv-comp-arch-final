# Vincent DeLuca
# 8/12/2022
# Advanced Computer Architecture
# Syracuse University

# based on the opcode, returns an instruction
def instruction_factory(opcode, arr, register_handler, address_handler):
    if opcode == "+":
        return AddInstruction(opcode, register_handler, arr[1], arr[2], arr[3])
    elif opcode == "+n":
        return AddImmediateInstruction(opcode, register_handler, arr[1], arr[2], arr[3])
    elif opcode == "==":
        return BranchOnEqualInstruction(opcode, register_handler, address_handler, arr[1], arr[2], arr[3])
    elif opcode == "!=":
        return BranchOnNotEqualInstruction(opcode, register_handler, address_handler, arr[1], arr[2], arr[3])
    elif opcode == "go":
        return JumpInstruction(opcode, address_handler, arr[1])
    elif opcode == "=n":
        return AddImmediateInstruction("+n", register_handler, arr[1], "$0", arr[2])
    elif opcode == "<":
        return SetLessThanInstruction(opcode, register_handler, arr[1], arr[2], arr[3])
    elif opcode == "<n":
        return SetLessThanImmediateInstruction(opcode, register_handler, arr[1], arr[2], arr[3])
    elif opcode == "-":
        return SubtractInstruction(opcode, register_handler, arr[1], arr[2], arr[3])
    else:
        raise ValueError(opcode)


# parent class of the instructions
class Instruction:
    def __init__(self, opcode):
        self.opcode = opcode

    def run(self):
        return

    def jump(self):
        return -1


# R instructions use registers
class RInstruction(Instruction):
    def __init__(self, opcode, register_handler, arg1, arg2, arg3):
        super().__init__(opcode)
        self.rd = register_handler.get(arg1)
        self.rs = register_handler.get(arg2)
        self.rt = register_handler.get(arg3)

    # returns a string of the opcode and three registers
    def print(self):
        opcode_print = self.opcode
        rs_print = self.rs.get_name()
        rt_print = self.rt.get_name()
        rd_print = self.rd.get_name()
        return f'{opcode_print}, {rd_print}, {rs_print}, {rt_print}\n'


# I instructions use two registers and a number
class IInstruction(Instruction):
    def __init__(self, opcode, register_handler, arg1, arg2, arg3):
        super().__init__(opcode)
        self.rt = register_handler.get(arg1)
        self.rs = register_handler.get(arg2)
        self.immediate = int(arg3)

    # returns a string of the opcode, two instructions, and number
    def print(self):
        opcode_print = self.opcode
        rs_print = self.rs.get_name()
        rt_print = self.rt.get_name()
        immediate_print = hex(self.immediate)
        return f'{opcode_print}, {rt_print}, {rs_print}, {immediate_print}\n'


# J instructions go to the address position
class JInstruction(Instruction):
    def __init__(self, opcode, address_handler, arg1):
        super().__init__(opcode)
        self.address = address_handler.get(f'{arg1}:')

    # returns a string of the opcode and the address
    def print(self):
        opcode_print = self.opcode
        address_print = hex(self.address)
        return f'{opcode_print}, {address_print}\n'


# simple addition instruction
class AddInstruction(RInstruction):
    def __init__(self, opcode, register_handler, arg1, arg2, arg3):
        super().__init__(opcode, register_handler, arg1, arg2, arg3)

    # adds the second and third register and sets it to the first register
    def run(self):
        self.rd.set_value(self.rs.get_value() + self.rt.get_value())


# simple addition instruction that takes a number
class AddImmediateInstruction(IInstruction):
    def __init__(self, opcode, register_handler, arg1, arg2, arg3):
        super().__init__(opcode, register_handler, arg1, arg2, arg3)

    # adds the second register and a number and sets it to the first register
    def run(self):
        self.rt.set_value(self.rs.get_value() + self.immediate)


# if the registers are equal, branch to address
class BranchOnEqualInstruction(IInstruction):
    def __init__(self, opcode, register_handler, address_handler, arg1, arg2, arg3):
        super().__init__(opcode, register_handler, arg1, arg2, address_handler.get(f'{arg3}:'))

    # if the registers aren't equal, return -1
    def jump(self):
        if self.rs.get_value() == self.rt.get_value():
            return self.immediate
        return -1


# if the registers are not equal, branch to address
class BranchOnNotEqualInstruction(IInstruction):
    def __init__(self, opcode, register_handler, address_handler, arg1, arg2, arg3):
        super().__init__(opcode, register_handler, arg1, arg2, address_handler.get(f'{arg3}:'))

    # if the registers are equal, return -1
    def jump(self):
        if self.rs.get_value() != self.rt.get_value():
            return self.immediate
        return -1


# go to the address
class JumpInstruction(JInstruction):
    def __init__(self, opcode, address_handler, arg1):
        super().__init__(opcode, address_handler, arg1)

    # return the address position
    def jump(self):
        return self.address


# set the first register to 1 if the second register is less than the third register
class SetLessThanInstruction(RInstruction):
    def __init__(self, opcode, register_handler, arg1, arg2, arg3):
        super().__init__(opcode, register_handler, arg1, arg2, arg3)

    # the boolean value is 1 for true and 0 for false
    def run(self):
        self.rd.set_value(self.rs.get_value() < self.rt.get_value())


# set the first register to 1 if the second register is less than the number
class SetLessThanImmediateInstruction(IInstruction):
    def __init__(self, opcode, register_handler, arg1, arg2, arg3):
        super().__init__(opcode, register_handler, arg1, arg2, arg3)

    # the boolean value is 1 for true and 0 for false
    def run(self):
        self.rt.set_value(self.rs.get_value() < self.immediate)


# simple subtraction instruction
class SubtractInstruction(RInstruction):
    def __init__(self, opcode, register_handler, arg1, arg2, arg3):
        super().__init__(opcode, register_handler, arg1, arg2, arg3)

    # subtracts the third register from the second register and sets it to the first register
    def run(self):
        self.rd.set_value(self.rs.get_value() - self.rt.get_value())
