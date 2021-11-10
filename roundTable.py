   
# The problem for this can be found here: https://www.codechef.com/ZCOPRAC/problems/ZCO12004.
  
def roundTable (N, A):

    arr = list(A)
    for i in range(2, N):
        arr[i] = arr[i] + min(arr[i-1], arr[i-2])

    valOne = arr[-1]
    arr = list(A)

    for i in range(N-3, -1, -1):
        arr[i] = arr[i] + min(arr[i+1], arr[i+2])
    
    return(min(valOne, arr[0]))

N = int(input())
A = list(map(int, input().split()))

print(roundTable(N, A))
   
