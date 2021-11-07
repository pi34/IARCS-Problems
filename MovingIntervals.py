  
# The problem can be found on this link: https://www.codechef.com/ZCOPRAC/problems/MOVINTRL.

def cake (C, N, K, P):

    duplicate = []
    finArr = []

    for arr in P:
        print(arr)
        if len(finArr) != 0:
            if arr[1] < finArr[0][0]:
                finArr.insert(0, arr)
            elif arr[0] > finArr[len(finArr)-1][1]:
                finArr.append(arr)
            else:
                if arr[0] <= finArr[len(finArr)-1][1]:
                    duplicate.append(arr[1] - arr[0] + 1)
                    duplicate.append(finArr[len(finArr)-1][1] - finArr[len(finArr)-1][0] + 1)
                    finArr.pop()
                elif arr[1] >= finArr[0][0]:
                    duplicate.append(arr[1] - arr[0] + 1)
                    duplicate.append(finArr[0][1] - finArr[0] + 1)
                    finArr.pop(0)

        else:
            finArr.append(arr)

    print(duplicate)

    if len(duplicate) is not K*2:
        return "Bad"

    available = []       

    if len(finArr) is 0:
        available.append(C)
    
    for i in range(len(finArr)):
        if i is 0:
            val = finArr[0][0]
            if val != 1:
                available.append(val-1)

        elif i is len(finArr)-1:
            val = finArr[i][1]
            if val != C:
                available.append(C-val)

        else:
            available.append(finArr[i][0] - finArr[i-1][1]-1)

    duplicate.sort(reverse=True)

    for dup in duplicate:
        available.sort()
        if dup > available[len(available)-1]:
            return "Bad"
        else:
            available[len(available)-1] = available[len(available)-1] - (dup[1] - dup[0] + 1)

    return "Good"

T = int(input())
N = list(map(int, input().split()))

L = []

for i in range(N[1]):
    A = list(map(int, input().split()))
    L.append(A)

print(L)

print(cake(N[0], N[1], N[2], L))
  
