from random import randint, random

from Mutation import Mutation

class OrderedMutation(Mutation) :
    
    def mutate(self, ind):
        chr = ind.chromosome
        n = len(chr)
        
        if random()<=self.prob:
            start = randint(0,n-1)
            end = randint(0,n-1)
            chr[start], chr[end] = chr[end],chr[start]

        ind.chromosome= chr


