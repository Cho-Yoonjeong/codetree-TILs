# l ~ r지점 : 구간 l ~ r-1

n = int(input())
A = [0] * 200
OFFSET = 100

for _ in range(n):
    l, r = map(int, input().split())
    for i in range(l, r):
        A[i+OFFSET] += 1

print(max(A))