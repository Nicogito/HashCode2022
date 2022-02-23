from random import randint
import OrderedIndividual as I
from copy import deepcopy
class Crossover :
    """
    Operator ordered crossover OX
    """
    def __init__(self):
        pass
    
    def apply (self, ind1, ind2) : 
        mom = deepcopy(ind1.chromosome)#deepcopy avoid write the current class of dad
        dad = deepcopy(ind2.chromosome)
        n = len(mom)

        start = randint(0,n-1)
        end = randint(start,n-1)

        chr1=[]
        chr2=[]

        mom_extr =mom[start:end+1]
        dad_extr =dad[start:end+1]

        #creation of the first child
        child1 = I.Individual(n)
        i=0
        while (i<start):
            e = dad.pop(0)
            if e not in mom_extr:
                chr1.append(e)
                i+=1

        chr1 += mom_extr

        i = end+1

        while (i<n):
            e = dad.pop(0)
            if e not in mom_extr:
                chr1.append(e)
                i+=1

        child1.chromosome=chr1

        #creation of the second child
        child2 = I.Individual(n)

        i=0
        while (i<start):
            e = mom.pop(0)
            if e not in dad_extr:
                chr2.append(e)
                i+=1

        chr2 += dad_extr

        i = end+1

        while (i<n):
            e = mom.pop(0)
            if e not in dad_extr:
                chr2.append(e)
                i+=1

        child2.chromosome=chr2

        return [child1, child2]

        
    