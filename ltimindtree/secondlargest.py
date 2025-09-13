a=input().split()


fl=int(min(a))
sl=int(min(a))
for i in a:
    i=int(i)
    if i>fl:
        sl=fl
        fl=i
        print(i,fl,sl)
    if i>sl and i!=fl:
        sl=i
        print(i,sl)
        

print(fl,sl)        




a=list(a)
a.sort()
print(a[len(a)-2])


