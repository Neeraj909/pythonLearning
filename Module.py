list=[]
for x in range(1,10):
    list.append(x**3)
print(list)
lst=[]
lst=[x**3 for x in range(1,11)]
print(lst)
lst1=[]
lst1=[x for x in range(2,21,2)]
print(lst1)

lst2=[]
lst2=[x for x in range(1,24,) if x%2==0]
print(lst2)


