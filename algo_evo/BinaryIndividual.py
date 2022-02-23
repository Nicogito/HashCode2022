from random import randint
from Individual import Individual

class BinaryIndividual(Individual) :
    """
    individual defined with an order / permutation
    """
    def __init__(self, n):
        super().__init__(n)

    def hydrateChrom(self, n):
        self.chromosome = [randint(0,1) for _ in range(n)]

    
