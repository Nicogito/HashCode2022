from random import shuffle
from Individual import Individual

class OrderedIndividual(Individual) :
    """
    individual defined with an order / permutation
    """
    def __init__(self, n):
        super().__init__(n)

    def hydrateChrom(self, n):
        self.chromosome = [_ for _ in range(n)]
        shuffle(self.chromosome)

    
