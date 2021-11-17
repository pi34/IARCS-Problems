# The problem for this can be found here: https://www.codechef.com/ZCOPRAC/problems/ZCO14002.

def SUPW (A, N):

    total = sum(A)
    arr = [0, 0, 0] + A

    for i in range(3, len(arr)):
        minima = min(arr[i-3], arr[i-2], arr[i-1])
        arr[i] = arr[i] + minima

    return min(arr[-1], arr[-2], arr[-3])

N = int(input())
A = list(map(int, input().split()))

print(SUPW(A, N))
