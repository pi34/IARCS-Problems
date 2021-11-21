
# The problem for this can be found here: https://www.codechef.com/ZCOPRAC/problems/ZCO13003.

I = list(map(int, input().split()))
A = list(map(int, input().split()))

A.sort()

i = 0
j = I[0]-1

numbers = 0

while i < j and j >= 0:

    if (A[i] + A[j]) < I[1]:
        numbers = numbers + (j-i)
        i = i + 1
    else:
        j = j - 1

print(numbers)
  
