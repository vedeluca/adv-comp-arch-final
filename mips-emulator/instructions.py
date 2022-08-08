from registers import Register


def instruction_factory(opcode="+", rs=Register(), rt=Register(), immediate=0, rd=Register(), shamt=0, funct="?",
                        address="?"):
    if opcode == "+":
        return RInstruction(opcode, rs, rt, rd, shamt, funct)
    elif opcode == "l":
        return IInstruction(opcode, rs, rt, immediate)
    elif opcode == "j":
        return JInstruction(opcode, address)
    else:
        raise ValueError(opcode)


class Instruction:
    def __init__(self, opcode):
        self.opcode = opcode


class RInstruction(Instruction):
    def __init__(self, opcode, rs, rt, rd, shamt, funct):
        super().__init__(opcode)
        self.rs = rs
        self.rt = rt
        self.rd = rd
        self.shamt = shamt
        self.funct = funct


class IInstruction(Instruction):
    def __init__(self, opcode, rs, rt, immediate):
        super().__init__(opcode)
        self.rs = rs
        self.rt = rt
        self.immediate = immediate


class JInstruction(Instruction):
    def __init__(self, opcode, address):
        super().__init__(opcode)
        self.address = address
