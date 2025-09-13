a=input()
b=[]
for i in a:
    if i not in b:
        print(i,end=" ")
        b.append(i)
        


a=set(a)
print(" ".join(a))

'''for i in range(len(a)):
    c=0
    for j in range(len(a)):
        if a[i]==a[j]:
            c+=1
    
        if c>1:
            print(a[i],end=" ")
            break 
    if c==1:
        print(a[i],end=" ")   '''     
