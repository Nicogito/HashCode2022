from time import time
import OrderedMutation as M
import OxCrossover as C
import Selection as S
import OrderedIndividual as I
import Problem as P
import Replacement as R

class EvoAlgo : 
    def __init__(self, nInd, maxIt,probMutation,  pathImg) :
        self.problem = P.Problem(pathImg)
        self.initPop(nInd)
        self.mutation = M.OrderedMutation(probMutation)#param : prob de mutation
        self.selection = S.Selection()
        self.crossover = C.Crossover()
        self.replacement = R.Replacement()

        self.MAX_IT = maxIt

        self.best = None

    
    def initPop(self, nInd):
        self.population = [self.problem.generateIndividual() for _ in range(nInd)]

    def run(self):
        t = time()
        self.f = open("stats.txt", "a")
        self.evalFunctions =0

        #evaluate initial population
        self.evalPop()

        while (self.evalFunctions<self.MAX_IT):
            
            mom = self.selection.select(self.population)
            dad = self.selection.select(self.population)

            childs = self.crossover.apply(mom, dad)

            for c in childs:
                self.mutation.mutate(c)

                self.evalInd(c)
            
            self.population = self.replacement.replace(self.population, childs)
        self.f.close()
        print ("TEMPS : ", time()-t)
        return self.best


    def evalPop(self) :
        for ind in self.population:
            self.evalInd(ind)

    def evalInd (self, ind):
        ind.fitness = self.problem.evaluate(ind)
        self.evalFunctions+=1
        self.checkIfBest(ind)
        #print(self.evalFunctions)

    def checkIfBest(self, ind):
        if self.best==None or self.best.fitness> ind.fitness:
            print("best found : ", ind.fitness)
            self.f.write(str(self.evalFunctions)+" "+str(ind.fitness)+"\n")
            self.best = ind

    def saveGenome(self):
        f = open("genome.txt", "w")
        res=""
        for e in self.population:
            res+= ",".join(list(map(str,e.chromosome)))+"\n"
        f.write(res)
        f.close()
