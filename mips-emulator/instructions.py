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
        opcode_hex = self.opcode.encode('utf-8').hex()
        rs_hex = self.rs.get_name().encode('utf-8').hex()
        rt_hex = self.rt.get_name().encode('utf-8').hex()
        rd_hex = self.rd.get_name().encode('utf-8').hex()
        shamt_hex = hex(self.shamt)
        funct_hex = hex(self.funct)
        return f'{opcode_hex}, {rs_hex}, {rt_hex}, {rd_hex}, {shamt_hex}, {funct_hex}'


class IInstruction(Instruction):
    def __init__(self, opcode="l", rs=Register(), rt=Register(), immediate=0):
        super().__init__(opcode)
        self.rs = rs
        self.rt = rt
        self.immediate = immediate

    def print(self):
        opcode_hex = self.opcode.encode('utf-8').hex()
        rs_hex = self.rs.get_name().encode('utf-8').hex()
        rt_hex = self.rt.get_name().encode('utf-8').hex()
        immediate_hex = hex(self.immediate)
        return f'{opcode_hex}, {rs_hex}, {rt_hex}, {immediate_hex}'


class JInstruction(Instruction):
    def __init__(self, opcode="j", address=None):
        super().__init__(opcode)
        self.address = address

    def print(self):
        opcode_hex = self.opcode.encode('utf-8').hex()
        address_hex = self.address.encode('utf-8').hex()
        return f'{opcode_hex}, {address_hex}'


class AddInstruction(IInstruction):
    def __init__(self, opcode, register_handler, arg1, arg2, arg3):
        rt = register_handler.get(arg1)
        rs = register_handler.get(arg2)
        immediate = int(arg3)
        super().__init__(opcode, rs, rt, immediate)

    def run(self):
        self.rt.set_value(self.rs.get_value() + self.immediate)
