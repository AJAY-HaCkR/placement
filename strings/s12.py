a=input()
res=[]

for i in range(len(a)):
    b=a[i]
    res.append(b)
    for j in range(i+1,len(a)):
        
        b+=a[j]
        res.append(b)
        

print(res)        