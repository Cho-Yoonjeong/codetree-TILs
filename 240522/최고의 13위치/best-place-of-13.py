N = int(input())
A = [
    list(map(int, input().split()))
    for _ in range(N)
]

max_cnt = 0
for i in range(N):
    for j in range(1, N-1):
        cnt = A[i][j-1] + A[i][j] + A[i][j+1]
        max_cnt = max(max_cnt, cnt)

print(max_cnt)