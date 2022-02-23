from abc import ABC, abstractmethod

class Individual():
    def __init__(self,n):
        self.fitness=0
        self.hydrateChrom(n)

    @abstractmethod
    def hydrateChrom(self, n):
        pass
    @abstractmethod
    def len(self):
        return len(self.chromosome)
    @abstractmethod
    def print(self):
        print ("{\n\tfitness = ",self.fitness,",\n\tchromosome = ",self.chromosome," \n}")