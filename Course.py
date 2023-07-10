class Course:
    def __init__(self,name,rating):
        self.name = name
        self.rating = rating
    def avgRating(self):
        number = len(self.rating)
        avg=sum(self.rating)/number
        print("AVG RATING",self.name," ",avg)

c1 = Course("Neeraj",[1,2,3,4,5])
print(c1.name)
print(c1.rating)
c1.avgRating()


