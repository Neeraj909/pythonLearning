a=[1,2,3,4,5]
b=[6,7,8,9,10]
z=[]
for i in range(0,len(a)):
    z.append(a[i]*b[i])
print(z)
z=[a[i]*b[i] for i in range(0,len(a))]
print(z)

c=[2,3,4,5,6,7]
d=[2,3,4,8,9,0]
e=[]
for i in c:
    if i in d:
        e.append(i)
print(e)
e=[i for i in c if i in d]
print(e)