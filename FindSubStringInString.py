s = "java is programing langauge"
sub = "programing"
found = False
pos = -1
length=len(s)
while True:
    pos=s.find(sub,pos+1,length)
    if pos == -1:
        break
    print("FOUND SUB AT POSITION",pos)
    found=True
if found == False:
    print("Sub String Not Found")