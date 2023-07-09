d={1:"A",2:"B",3:"C",8:"D",7:"E",6:"F"}
print(d)
print(d.items())
print(d.keys())
print(d.values())
print(d[3])
del d[3]
print(d)
a=12
b=23
print(a is b)
print(id(a))
print(id(b))
stu={"A":["Java","OOPS","MAP"],"B":["Java","COLLECTIO","SET"],"C":["Java","STRING","LIST"]}
keys=stu.keys()
for eachKay in keys:
    print("course",eachKay,"HAAN")
    for eachBacha in stu[eachKay]:
        print(eachBacha)