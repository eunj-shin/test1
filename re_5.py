# 숙제  
result = 1

for i in range(1,6):
    result *= i
    continue
print(result)



# 강의
def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)

result = fact(5)
print(result)






# 추가 문제 - 피보나치수열
"""
    --- 0 (n=1)
f(n)--- 1 (n=2)
    --- f(n-2) + f(n-1)
"""


# 추가 문제 풀이
l = []
def fibo(n):
    if n == 1:
        return 0
    elif n <= 2:
        return 1
    elif n > 2:
        return (fibo(n-2)+fibo(n-1))

for i in range(1,11,1):
    print(i,fibo(i))


# 추가 문제풀이 2
l = [a, b]
for i in l:
    if a == 1:
        return 0
    elif a == 2:
        return 1
    elif n > 2:
        l.append(l[len(l)-1])



# 추가 문제풀이 2
l = [0, 1]
for i in range(10):
    val = l[-2] + l[-1]
    l.append[val]
print(1)






time python fib2.py #시간 확인
import sys

num = int(sys.argv[1])


