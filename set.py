s={4,5,6,1,344,44,55,33,22,11,3,2,4,5,6,33,22}
print(s)
print(type(s))
s.update([66,99])
print(s)
# print(s[0])
# set object dose not support indexing
# print(s*3)
# set object dose not support slicing or repetatin
s.remove(4)
print(s)
f=frozenset(s)
print(f)


