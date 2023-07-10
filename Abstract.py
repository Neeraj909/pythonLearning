from abc import abstractmethod,ABC
class BMW(ABC):
    @abstractmethod
    def drive(self):
        pass
class Audi(BMW):
    def drive(self):
        print("BMW TO AUDI")
a=Audi()
a.drive()
