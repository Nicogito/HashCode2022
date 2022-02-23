from random import randint
class Selection : 

    """
    Tournament selection
    """

    def select (self, pop):
        n = len(pop)

        idx=randint(0,n-1)
        idy=randint(0,n-1)

        if pop[idx].fitness > pop[idy].fitness:
            return pop[idx]
        return pop[idy]