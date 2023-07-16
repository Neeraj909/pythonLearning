import logging
logging.basicConfig(filename="mylog.log",level=logging.DEBUG)
# class OverTheLimitOfExcption(Exception):
#     def __init__(self,msg):
#         self.msg = msg
# def withdrow(amount):
#         if(amount>500):
#             raise OverTheLimitOfExcption("can not with drwo more than 500")

class TwoYoung(Exception):
    def __init__(self,msg):
        self.msg = msg
class TwoOld(Exception):
    def __init__(self,msg):
        self.msg = msg
age = int(input("Enter age"))
if age<18:
    raise TwoYoung("Chota hai bc ke")
elif age>90:
    raise TwoOld("Bhut bada hau re tu")
else:
    print("tu thek hai ")

