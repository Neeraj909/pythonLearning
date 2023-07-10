# s="neeraj"
# print(s)
# print(s[::-1])
# s="sharma"
# i = len(s)-1
# result = ''
# while i >= 0:
#     result = result+s[i]
#     i = i-1
s = "java is programing language"
temp=s.split()
result=[]
i=len(temp)-1
while i >= 0:
    result.append(temp[i])
    i=i-1
print(result)
s = "java is programing language"
temp=s.split()
i=0
result=[]
while i<len(temp):
    result.append(temp[i][::-1])
    i=i+1
print(result)
s='aavvdddddffwweqewvfbttrgrgeeeeferf'






