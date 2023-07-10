class Programmer:

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setSal(self, sal):
        self.sal = sal

    def getSal(self):
        return self.sal

    def setTech(self, tech):
        self.tech = tech

    def getTech(self):
        return self.tech
p1=Programmer()
p1.setName("Neeraj")
p1.setSal(20000)
p1.setTech(["java","Python","GO"])
print(p1.getName())
print(p1.getSal())
print(p1.getTech())