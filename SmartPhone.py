  
# The problem can be found on this link: https://www.codechef.com/ZCOPRAC/problems/ZCO14003.

num = int(input())

A = []

for _ in range(num):
    A.append(int(input()))

(A).sort(reverse=True)

new = []
for i in range(len(A)):
    new.append(A[i]*(i+1))

print(max(new))
  
