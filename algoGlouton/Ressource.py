class Ressource : 
    def __init__(self, name, skills) -> None:
        self.name = name
        self.skills = skills
        self.available = True

    def updateSkills(self, skill):#string de skill
        self.skills[skill]+=1

    def toString(self):

        return self.name + " : " + str(self.skills) + " : " + str(self.available)
    