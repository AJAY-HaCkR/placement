a=input().strip()
b=input().strip()
if len(a)!=len(b):
    print(False)
sum1=0
sum2=0
for i in range(len(a)):
    sum1+=ord(a[i])

for j in range(len(b)):
    sum2+=ord(b[j])

if sum1==sum2:
    print("Anagarm")        
