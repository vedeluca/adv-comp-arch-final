# Vincent DeLuca
# 9/18/2022
# Advanced Computer Architecture
# Syracuse University

# based on the opcode, returns an instruction
def instruction_factory(arr):
    opcode = arr[0]
    if opcode == "add":
        return AddInstruction(opcode, arr[1], arr[2], arr[3])
    elif opcode == "lw":
        return LoadWordInstruction(opcode, arr[1], arr[3], arr[2])
    elif opcode == "sw":
        return StoreWordInstruction(opcode, arr[1], arr[3], arr[2])
    elif opcode == "sub":
        return SubtractInstruction(opcode, arr[1], arr[2], arr[3])
    else:
        raise ValueError(opcode)


# parent class of the instructions
class Instruction:
    def __init__(self, opcode):
        self.opcode = opcode
        self.hazard = ""
        self.hazard_location = 0

    def print(self):
        return list(self.opcode)

    def problem(self):
        raise AttributeError

    def check_for_hazard(self, problems):
        raise AttributeError


class RInstruction(Instruction):
    def __init__(self, opcode, arg1, arg2, arg3):
        super().__init__(opcode)
        self.rd = arg1
        self.rs = arg2
        self.rt = arg3

    def print(self):
        arr = list()
        arr.append(self.opcode)
        arr.append(self.rs)
        arr.append(self.rt)
        arr.append(self.rd)
        return arr

    def problem(self):
        return self.rd

    def check_for_hazard(self, problems):
        for i, problem in reversed(list(enumerate(problems))):
            if problem in (self.rs, self.rt, self.rd):
                self.hazard = problem
                self.hazard_location = i
                return True
        return False


class IInstruction(Instruction):
    def __init__(self, opcode, arg1, arg2, arg3):
        super().__init__(opcode)
        self.rt = arg1
        self.rs = arg2
        self.immediate = arg3

    def print(self):
        arr = list()
        arr.append(self.opcode)
        arr.append(self.rs)
        arr.append(self.rt)
        arr.append("")
        arr.append(self.immediate)
        return arr

    def problem(self):
        return self.rt

    def check_for_hazard(self, problems):
        for i, problem in reversed(list(enumerate(problems))):
            if problem == self.rt:
                self.hazard = problem
                self.hazard_location = i
                return True
        return False


class JInstruction(Instruction):
    def __init__(self, opcode, arg1):
        super().__init__(opcode)
        self.address = arg1


class AddInstruction(RInstruction):
    def __init__(self, opcode, arg1, arg2, arg3):
        super().__init__(opcode, arg1, arg2, arg3)


class LoadWordInstruction(IInstruction):
    def __init__(self, opcode, arg1, arg2, arg3):
        super().__init__(opcode, arg1, arg2, arg3)


class StoreWordInstruction(IInstruction):
    def __init__(self, opcode, arg1, arg2, arg3):
        super().__init__(opcode, arg1, arg2, arg3)


class SubtractInstruction(RInstruction):
    def __init__(self, opcode, arg1, arg2, arg3):
        super().__init__(opcode, arg1, arg2, arg3)
