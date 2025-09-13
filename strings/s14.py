a=input().split()

for i in a:
    b=""
    for j in range(1,len(i)):
        b+=i[j]
    i=i[0].upper()+b
    print(i,end=" ")
      
