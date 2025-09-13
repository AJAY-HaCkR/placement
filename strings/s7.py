a=input()
res=""
max=0
for i in range(len(a)):
    c=0
    for j in range(len(a)):
        if a[i]==a[j]:
            c+=1
    if c>max:
        max=c
        res=a[i]


print(res,max)        

