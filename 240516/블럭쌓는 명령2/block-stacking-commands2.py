N, K = map(int, input().split())

A = [0] * (N+1)

for _ in range(K):
    l, r = map(int,input().split())
    for i in range(l, r+1):
        A[i] += 1

print(max(A))