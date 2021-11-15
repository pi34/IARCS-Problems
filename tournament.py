# The problem for this canbe found here: https://www.codechef.com/ZCOPRAC/problems/ZCO13001.

N = int(input())
A = list(map(int, input().strip().split()))

tSum = 0
total = sum(A)
length = N

A.sort()

for i in range(N):
    total = total - A[i]
    length = length - 1
    tSum = tSum + abs(total - ((length)*A[i]))

print(tSum)
