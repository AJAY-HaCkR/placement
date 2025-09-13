def fibonacci(n):
    if n<=1:
        return n
    
    return fibonacci(n-1)+fibonacci(n-2)
    
num1=0
num2=1
sum=0
a=int(input())
#print(0,1)
for i in range(a):
    sum=num1+num2
    print(num1)
    num1=num2
    num2=sum
for i in range(a):
    print("fib",fibonacci(i))

