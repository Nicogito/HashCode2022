from importlib import resources


class Project : 
    def __init__(self, name, skills, score, deadline, duree) -> None:
        self.name = name
        self.skills = skills#dictionnaire
        self.score = score
        self.deadline = deadline
        self.ressources=[]
        self.duree = duree
        self.startTime=-1

    def addRessource(self, ressource):
        self.ressources.append(ressource)

    def toString(self):

        return self.name + " : " + str(self.skills) + " : " + str(self.score) + " : " + str(self.deadline) + " : " + str(self.duree) + " : nbCollab : " + str(len(self.ressources))