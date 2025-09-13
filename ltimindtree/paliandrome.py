a=input()
b=a[::-1]
if a==b:
    print("paliandrome")

mid=int(len(a)/2)
print(mid)

for i in range(0,mid):
    
    if a[i]!=a[len(a)-i-1]:
        print(False)
        break

else:
    print(True)        
            