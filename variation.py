
# The problem for this can be found here: https://www.codechef.com/ZCOPRAC/problems/ZCO15002.

specs = list(map(int, input().strip().split()))
A = list(map(int, input().strip().split()))

leastCount = 0
i = 0
j = 0

A.sort()
while j < specs[0]:
    while (A[j] - A[i]) >= specs[1]:
        leastCount = leastCount + (specs[0]-j)
        i = i + 1
    j = j + 1

print(leastCount)
