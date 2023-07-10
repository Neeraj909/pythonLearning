x = int(input("enter a number"))
if x==0:
    print(x,"is zero")
elif x % 2 == 0:
    print(x, "is even numver")
else:
    print(x, "is odd numver")

while(x > 0):
    print(x)
    x-=1
x=7
for i in range(x):
    if i==3:
        break
    if i%2==0:
        continue
    print(i)

word = input("enter a word")
vowels = {'a','e','i','o','u'}
result = {}
for c in word:
    if c in vowels:
        result[c]=result.get(c,0)+1

for k,v in result.items():
    print(k,"is present",v,"times")




