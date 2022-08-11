# TODO: figure out how to output more than one instruction
def instruction_factory(opcode, register_handler, arg1, arg2, arg3):
    if opcode == "add":
        return AddInstruction(opcode, register_handler, arg1, arg2, arg3)
    elif opcode == "addi":
        return AddImmediateInstruction(opcode, register_handler, arg1, arg2, arg3)
    elif opcode == "slt":
        return SetLessThanInstruction(opcode, register_handler, arg1, arg2, arg3)
    elif opcode == "slti":
        return SetLessThanImmediateInstruction(opcode, register_handler, arg1, arg2, arg3)
    elif opcode == "sub":
        return SubtractInstruction(opcode, register_handler, arg1, arg2, arg3)
    else:
        raise ValueError(opcode)


class Instruction:
    def __init__(self, opcode):
        self.opcode = opcode


class RInstruction(Instruction):
    def __init__(self, opcode, register_handler, arg1, arg2, arg3):
        super().__init__(opcode)
        self.rd = register_handler.get(arg1)
        self.rs = register_handler.get(arg2)
        self.rt = register_handler.get(arg3)

    def print(self):
        opcode_print = self.opcode
        rs_print = self.rs.get_name()
        rt_print = self.rt.get_name()
        rd_print = self.rd.get_name()
        return f'{opcode_print}, {rd_print}, {rs_print}, {rt_print}\n'


class IInstruction(Instruction):
    def __init__(self, opcode, register_handler, arg1, arg2, arg3):
        super().__init__(opcode)
        self.rt = register_handler.get(arg1)
        self.rs = register_handler.get(arg2)
        self.immediate = int(arg3)

    def print(self):
        opcode_print = self.opcode
        rs_print = self.rs.get_name()
        rt_print = self.rt.get_name()
        immediate_print = hex(self.immediate)
        return f'{opcode_print}, {rt_print}, {rs_print}, {immediate_print}\n'


class JInstruction(Instruction):
    def __init__(self, opcode, arg1):
        super().__init__(opcode)
        self.address = arg1

    def print(self):
        opcode_print = self.opcode
        address_print = self.address
        return f'{opcode_print}, {address_print}\n'


class AddInstruction(RInstruction):
    def __init__(self, opcode, register_handler, arg1, arg2, arg3):
        super().__init__(opcode, register_handler, arg1, arg2, arg3)

    def run(self):
        self.rd.set_value(self.rs.get_value() + self.rt.get_value())


class AddImmediateInstruction(IInstruction):
    def __init__(self, opcode, register_handler, arg1, arg2, arg3):
        super().__init__(opcode, register_handler, arg1, arg2, arg3)

    def run(self):
        self.rt.set_value(self.rs.get_value() + self.immediate)


class SetLessThanInstruction(RInstruction):
    def __init__(self, opcode, register_handler, arg1, arg2, arg3):
        super().__init__(opcode, register_handler, arg1, arg2, arg3)

    def run(self):
        self.rd.set_value(self.rs.get_value() < self.rt.get_value())


class SetLessThanImmediateInstruction(IInstruction):
    def __init__(self, opcode, register_handler, arg1, arg2, arg3):
        super().__init__(opcode, register_handler, arg1, arg2, arg3)

    def run(self):
        self.rt.set_value(self.rs.get_value() < self.immediate)


class SubtractInstruction(RInstruction):
    def __init__(self, opcode, register_handler, arg1, arg2, arg3):
        super().__init__(opcode, register_handler, arg1, arg2, arg3)

    def run(self):
        self.rd.set_value(self.rs.get_value() - self.rt.get_value())
