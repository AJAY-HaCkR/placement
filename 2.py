a=input()
b=[]
c=""
d=0
for i in a:
    b.append(i)
for j in range(len(b)):
    if b[j].isalpha():
        c+=str(b[j])
    if b[j].isdigit():
        d=d+int(b[j])

print(d,c)            
