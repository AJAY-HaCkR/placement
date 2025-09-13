a=input()
res=""
for i in a:
    c=0
    for j in a:
        if i==j:
            c+=1
    if c>0:       
        res+=i+str(c)
        a=a.replace(i,"")        
    
print(res)