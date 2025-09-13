a=input()
b=""
for i in range(len(a)):
    if a[i].isdigit():
        continue
    else:
        b+=a[i]
        


print(b)        
