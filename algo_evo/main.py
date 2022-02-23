import EvoAlgo as ea
#path to img
path = "images/img0-shuffled.txt"
#mutation probability
probMutation = 0.7

#instance of EA
algo = ea.EvoAlgo(50, 100, probMutation,path)

#run the search
sol = algo.run()

#Save the genome (tranfer learning)
#algo.saveGenome()


sol.print()
#save the solution
f = open("result.txt", "w")

for a in sol.chromosome:
    f.write(str(a)+";")


