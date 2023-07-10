#Duck Typing
class Duck:
    def talk(self):
        print("DUCK DUCK")
class Human:
    def talk(self):
        print("Chal be")

def callTalk(obj):
    obj.talk()
d=Duck()
callTalk(d)
h=Human()
callTalk(h)