from random import randint, random

from Mutation import Mutation

class BinaryMutation(Mutation) :
    
    def mutate(self, ind):
        chr = ind.chromosome
        n = len(chr)
        for i in range(chr):
            if random()<=self.prob:
                chr[i]= 1 - chr[i]

        ind.chromosome= chr


