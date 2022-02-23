class Replacement :
    """
    Elitist replacement.
    """
    
    def __init__(self) -> None:
        pass

    def sortList(self, array):
        for item in range(len(array)):
            for j in range(0, (len(array) - item - 1)):
                if array[j].fitness > array[j + 1].fitness:
                    (array[j], array[j + 1]) = (array[j + 1], array[j])

    def replace(self,pop, childs):
        newpop = pop + childs
        #newpop.sort(key=lambda x: x.fitness, reverse=False)
        self.sortList(newpop)
        return newpop[:len(pop)]

