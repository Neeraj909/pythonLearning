


class Encapsulation:
    def setId(self,id):
        self.id = id

    def getId(self):
        return self.id

    def setName(self,name):
        self.name = name

    def getName(self):
        return self.name


e = Encapsulation()
e.setId(1)
e.setName('Neeraj')
print(e.getId())
print(e.getName())