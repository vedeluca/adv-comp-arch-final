# Vincent DeLuca
# 9/20/2022
# Advanced Computer Architecture
# Syracuse University

from instructions import *


class TimingDiagram:
    def __init__(self):
        self._pipelines = list()

    def print(self):
        return [pipeline.print() for pipeline in self._pipelines]


class TimingDiagramWithoutForwardingUnit(TimingDiagram):
    def __init__(self):
        super().__init__()


class TimingDiagramWithForwardingUnit(TimingDiagram):
    def __init__(self):
        super().__init__()


class Pipeline:
    def __init__(self):
        self._instruction = Instruction("")
        self._pipes = list()

    def print(self):
        return [pipe.print() for pipe in self._pipes]


class Pipe:
    def __init__(self):
        self._problem_row = 0
        self._problem_column = 0

    def print(self):
        raise AttributeError

    def set_problem(self, row, column):
        self._problem_row = row
        self._problem_column = column

    def get_problem_line(self):
        return [self._problem_row, self._problem_column]


class FetchPipe(Pipe):
    def __init__(self):
        super().__init__()

    def print(self):
        return "F"


class DecodePipe(Pipe):
    def __init__(self):
        super().__init__()

    def print(self):
        return "D"


class ExecutePipe(Pipe):
    def __init__(self):
        super().__init__()

    def print(self):
        return "X"


class MemoryPipe(Pipe):
    def __init__(self):
        super().__init__()

    def print(self):
        return "M"


class WritePipe(Pipe):
    def __init__(self):
        super().__init__()

    def print(self):
        return "W"


class StallPipe(Pipe):
    def __init__(self):
        super().__init__()

    def print(self):
        return "S"
