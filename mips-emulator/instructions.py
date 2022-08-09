from registers import *


def instruction_factory(opcode, register_handler, arg1, arg2, arg3):
    if opcode == "+":
        return AddInstruction(opcode, register_handler, arg1, arg2, arg3)
    else:
        raise ValueError(opcode)


class Instruction:
    def __init__(self, opcode):
        self.opcode = opcode


class RInstruction(Instruction):
    def __init__(self, opcode="+", rs=Register(), rt=Register(), rd=Register(), shamt=0, funct=0):
        super().__init__(opcode)
        self.rs = rs
        self.rt = rt
        self.rd = rd
        self.shamt = shamt
        self.funct = funct

    def print(self):
        opcode_print = self.opcode
        rs_print = self.rs.get_name()
        rt_print = self.rt.get_name()
        rd_print = self.rd.get_name()
        shamt_print = hex(self.shamt)
        funct_print = hex(self.funct)
        return f'{opcode_print}, {rs_print}, {rt_print}, {rd_print}, {shamt_print}, {funct_print}\n'


class IInstruction(Instruction):
    def __init__(self, opcode="l", rs=Register(), rt=Register(), immediate=0):
        super().__init__(opcode)
        self.rs = rs
        self.rt = rt
        self.immediate = immediate

    def print(self):
        opcode_print = self.opcode
        rs_print = self.rs.get_name()
        rt_print = self.rt.get_name()
        immediate_print = hex(self.immediate)
        return f'{opcode_print}, {rs_print}, {rt_print}, {immediate_print}\n'


class JInstruction(Instruction):
    def __init__(self, opcode="j", address=None):
        super().__init__(opcode)
        self.address = address

    def print(self):
        opcode_print = self.opcode
        address_print = self.address
        return f'{opcode_print}, {address_print}\n'


class AddInstruction(IInstruction):
    def __init__(self, opcode, register_handler, arg1, arg2, arg3):
        rt = register_handler.get(arg1)
        rs = register_handler.get(arg2)
        immediate = int(arg3)
        super().__init__(opcode, rs, rt, immediate)

    def run(self):
        self.rt.set_value(self.rs.get_value() + self.immediate)
