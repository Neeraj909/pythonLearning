x=123
def display():
    x=23
    print(x)
    print(globals()['x'])
print(x)
display()
z= display
print(z())

def name(name):
    def message():
        return "Hello "
    result=message()+name
    return result
print(name("Neeraj"))

def fun(name):
    return "Hello"+name
def name():
    return "Neeraj"
print(fun(name()))
