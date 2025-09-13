a =list(input().strip())
j=0
for i in a:
    c=0
    for j in range(len(a)):
        if i==a[j]:
            c+=1
         

    if c<2:
        print(i)          