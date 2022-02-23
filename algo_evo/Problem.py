import numpy as np
import OrderedIndividual as I

class Problem :
    def __init__(self, pathImg):
        self.data = np.loadtxt(pathImg)
        self.problemSize = self.data.shape[0]

    def generateIndividual(self):
        return I.OrderedIndividual(self.problemSize)


    def evaluate(self, ind):
        res = 0
        chr = ind.chromosome

        for i in range(self.problemSize-1):
            res+= np.linalg.norm(self.data[chr[i]]-self.data[chr[i+1]], axis=0)
        
        return res
        