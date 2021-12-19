def pitches(n):

    scores = []
    l = []
    u = []

    for i in range(len(n)):
        scores.append(0)
        l.append([n[i][0], i])
        u.append([n[i][1], i])

    l.sort()
    u.sort()

    for i in range(len(n)):
        ind = u[i][1]
        scores[ind] = scores[ind] + i
        ind = l[len(n)-i-1][1]
        scores[ind] = scores[ind] + i   

    return scores

T = int(input())

for _ in range(T):
    N = int(input())

    L = []

    for i in range(N):
        A = list(map(int, input().split()))
        L.append(A)

    print(' '.join(map(str, pitches(L))))
