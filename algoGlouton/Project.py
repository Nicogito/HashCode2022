class Project : 
    def __init__(self, name, skills, score, deadline) -> None:
        self.name = name
        self.skills = skills#dictionnaire
        self.score = score
        self.deadline = deadline
        self.ressources=[]

    def addRessource(self, ressource):
        self.ressources.append(ressource)

