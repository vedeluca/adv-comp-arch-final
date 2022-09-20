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

    def _add_pipeline(self, instruction):
        pipeline = Pipeline(instruction)
        if len(self._pipelines) == 0:
            pipeline.first_pipeline()
            self._pipelines.append(pipeline)
            return None
        else:
            previous = self._pipelines[-1]
            i = previous.get_decode()
            pipeline.set_fetch(i)
            return pipeline


class TimingDiagramWithoutForwardingUnit(TimingDiagram):
    def __init__(self):
        super().__init__()

    def add_pipeline(self, instruction):
        pipeline = self._add_pipeline(instruction)
        if pipeline is None:
            return
        self._pipelines.append(pipeline)


class TimingDiagramWithForwardingUnit(TimingDiagram):
    def __init__(self):
        super().__init__()

    def add_pipeline(self, instruction):
        pipeline = self._add_pipeline(instruction)
        if pipeline is None:
            return
        self._pipelines.append(pipeline)


class Pipeline:
    def __init__(self, instruction):
        self._instruction = instruction
        self._pipes = list()

    def print(self):
        return self._pipes

    def add_pipe(self, pipe):
        self._pipes.append(pipe)

    def first_pipeline(self):
        self.add_pipe("F")
        self.add_pipe("D")
        self.add_pipe("X")
        self.add_pipe("M")
        self.add_pipe("W")

    def get_decode(self):
        return self._pipes.index("D")

    def set_fetch(self, index):
        for i in range(index):
            self.add_pipe("")
        # self.add_pipe("F")
        self.first_pipeline()
