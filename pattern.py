n=int(input("number of rows"))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print('*',end="")
#     print()
# by single for loop
for i in range(1,n+1):
    print("*"*i)
# *
# * *
# * * *
# * * * *
# * * * * *
n1=int(input("number of rows"))
for i in range(1,n+1):
    print(" "*(n-1),end="")
    print("* "*i)
