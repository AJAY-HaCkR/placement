nums=list(input().split())
a=[i for i in range(1,len(nums)+2)]
b=[]
nums.sort()
for i in nums:
    for j in a:
        if int(i)==j:
            a.remove(int(i))


print(min(a))            
#print(a)
#print(nums)
#nums = list(map(int, input("Enter numbers: ").split()))
'''n = len(nums) + 1
expected = set(range(1, n + 1))
actual = set(nums)
missing = expected - actual
print(min(missing))'''