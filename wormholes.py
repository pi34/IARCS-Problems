   
# The problem for this can be found here: https://www.codechef.com/ZCOPRAC/problems/ZCO12002.

def wormholes (N, X, Y, A1, A2, A3):

    A2.sort()
    A3.sort()

    def exit (A, start, end, value):

        if end >= start:

            mid = (end+start)//2

            if mid is Y:
                return A[mid]

            if A[mid] == value:
                return A[mid]
            
            if value < A[mid] and value > A[mid-1]:
                return A[mid]

            elif A[mid] > value:
                return exit(A, start, mid - 1, value)

            else:
                return exit(A, mid + 1, end, value)

        else:
            return -1

    def arrive (A, start, end, value):

        if end >= start:

            mid = (end+start)//2

            if mid is 0:
                return A[mid]

            if A[mid] == value:
                return A[mid]

            if value < A[mid] and value > A[mid-1]:
                return A[mid-1]

            elif A[mid] > value:
                return arrive(A, start, mid - 1, value)

            else:
                return arrive(A, mid + 1, end, value)

        else:
            return -1

    times = []

    for i in range(N):

        strt = arrive([0] + A2, 0, X, A1[i][0])
        nd = exit([0] + A3, 0, Y, A1[i][1])

        print(strt, nd)

        times.append(nd-strt+1)

    return min(times)


print(wormholes(3, 4, 2, [[15, 21], [5, 10], [7, 25]], [4, 14, 25, 2], [13, 21]))
   
# Expected Output: 8
  
