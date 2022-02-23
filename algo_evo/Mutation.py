from abc import ABC, abstractmethod

class Mutation(ABC):

    def __init__(self, prob):
        self.prob = prob
    
    @abstractmethod
    def mutate(self, ind):
        pass