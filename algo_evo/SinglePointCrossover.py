from copy import deepcopy
from random import randint
import BinaryIndividual as I

class SinglePointCrossover :
    def __init__(self) -> None:
        pass

    def apply (self, ind1, ind2) : 
        mom = deepcopy(ind1.chromosome)#deepcopy avoid write the current class of dad
        dad = deepcopy(ind2.chromosome)
        n = len(mom)

        idx = randint(0,n-1)

        chr1=mom[:idx]+dad[idx:]
        chr2=dad[:idx]+mom[idx:]

        child1 = I.Individual(n)
        child1.chromosome= chr1

        child2 = I.Individual(n)
        child2.chromosome= chr2

        return [child1, child2]
