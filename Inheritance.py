class Inheritance:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year

    def start(self):
        print("Car Chal")

    def stop(self):
        print("Car Ruk Ja")
class ThreeSeriesSow(Inheritance):
    def __init__(self,control,make,model,year):
       # Inheritance.__init__(self,make,model,year)
       super().__init__(make,model,year)
       self.control = control

    def start(self):
        print("Car Chalu By Button")
class FiveSeriesSow(Inheritance):
    def __init__(self,parking,make,model,year):
        Inheritance.__init__(self,make,model,year)
        self.parking=parking

        def stop(self):
           print("Car Ruk By Button")


threeSeries=ThreeSeriesSow(True,"BWM",3421,2022)
print(threeSeries.control)
print(threeSeries.year)
print(threeSeries.make)
print(threeSeries.model)
threeSeries.start()
threeSeries.stop()
