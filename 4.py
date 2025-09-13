
num=list(map(int,input().strip()))
#print(num)
#print(len(num))
a=[i for i in range(1,len(num)+2)]
#print(a)
es=sum(a)
asu=sum(num)
print(es-asu)