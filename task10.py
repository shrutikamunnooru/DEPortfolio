'''
You are tasked with creating a system to manage and process data from various data pipelines.
Each data pipeline represents a sequence of data processing steps. You will implement classes to represent pipelines, 
steps, and the data processed. Your system should be able to add, remove, and execute steps in a pipeline.
'''

class Databatch:
    def __init__(self, data):
        self.data = data

class PipelineStep:
    def __init__(self, name):
        self.name = name
    
    def process(self, data_batch):
        raise NotImplementedError("Subclasses must override process() method")

class DataPipeline:
    def __init__(self, name, steps):
        self.name = name
        self.steps = []

    def add_step(self, step):
        self.steps.append(step)
        
    def remove_step(self, step_name):
        self.steps.remove(step_name)

    def execute(self, data_batch):
        for step in self.steps:
            step.process(data_batch)

class FilterStep(PipelineStep):
    def __init__(self, name, condition):
        self.name = name
        self.condition = condition
    
    def process(self, data_batch):
        data_batch.data = [x for x in data_batch.data if self.condition(x)]

class TransformStep(PipelineStep):
    def __init__(self,name, transformation):
        self.name = name
        self.transformation = transformation
    
    def process(self, data_batch):
        data_batch.data = [self.transformation(x) for x in data_batch.data]

        















    

















