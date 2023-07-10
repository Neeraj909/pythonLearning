def fun(list):
    for i in list:
        print(i,end="")
fun([1,2,3,4])
print()

def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))