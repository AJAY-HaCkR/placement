from collections import defaultdict

def f(j):
    ch=0
    for i in j:
        ch+=ord(i)

    return ch    




a=list(input().split())
dict=defaultdict(list)
b=0
for i in a:
   b=f(i)
   dict[b].append(i)

print( list(dict.values()))




