from Ressource import *
from Project import *
f = open("../input_data/a.txt", "r")
lines=f.readlines()
f.close()

nbContributors, nbProjects = list(map(int,lines[0].split(" ")))

projects = []
ressources=[]
availableRessources=[]

dictS = set()
idx=1
for i in range(nbContributors):
    nbS = int(lines[idx].split()[1])
    idx+=1
    for j in range(nbS):
        dictS.add(lines[idx].split()[0])
        idx+=1
print(dictS)


def remplirDico(dictS):
    x = {}
    for i in dictS:
        x[i] = 0
    return x

dicoVide = remplirDico(dictS)
idx=1
for i in range(nbContributors):
    nbS = int(lines[idx].split()[1])
    nom = lines[idx].split()[0]
    idx+=1
    dico = dicoVide.copy()
    
    for j in range(nbS):
        l = lines[idx].split()
        dico[l[0]] = int(l[1])
        idx+=1
    ressources.append(Ressource(nom,dico))

for i in range(nbProjects):
    nbS = int(lines[idx].split()[4])
    nom = lines[idx].split()[0]
    temps = int(lines[idx].split()[1])
    score = int(lines[idx].split()[2])
    deadline = int(lines[idx].split()[3])
    idx+=1
    dico = {}
    for j in range(nbS):
        l = lines[idx].split()
        dico[l[0]] = int(l[1])
        idx+=1
    projects.append(Project(nom,dico,score,deadline,temps))

print(dictS)
print(ressources[0].toString())
print(projects[0].toString())
