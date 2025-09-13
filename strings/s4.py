a=input()
b="aeiouAEIOU"
c=0
d=0
for i in a:
    if i in b:
        c+=1
    else:
        d+=1

print("vowels",c,"consonants",d)            