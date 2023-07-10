from functools import  reduce
def cube(n):
    return  n**3
print(cube(2))

f=lambda n:n**3
print("lambda",f(3))
l=lambda x:'yes' if x%2==0 else 'no'
print(l(10))
print(l(9))
sum=lambda a,b:a+b
print(sum(10,10))
lst=[10,2,3,4,5,7,8,0,1,2,3,4,5,6,7]
result=filter(lambda x:x%2==0,lst)
print(list(result))
result1=list(map(lambda n:n*2,lst))
print(result1)
result2=reduce(lambda x,y:x+y,lst)
print(result2)


