class Product:
    def __init__(self):
        self.name="Iphone"
        self.Desc="Good"
        self.price=10000
    def display(self):
        print(self.name," ",self.Desc," ",self.price)
p1 = Product()
p1.display()
print(p1.Desc)
print(p1.price)
print(p1.name)


