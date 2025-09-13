a=input()
b=input()
a=list(a)
b=list(b)

if len(a)!=len(b):
    print("Not anagram")
    exit()
a.sort()
b.sort()
for i in range(len(a)):
    if a[i]!=b[i]:
        print("not anagram")
        break
        exit()   


print("Anagram")
