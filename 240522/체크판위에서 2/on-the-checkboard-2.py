R, C = map(int, input().split())
A = [
    input().split()
    for _ in range(R)
]

cnt = 0
for r1 in range(1, R):
    for c1 in range(1, C):
        for r2 in range(r1+1, R-1):
            for c2 in range(c1+1, C-1):
                if A[0][0] != A[r1][c1] != A[r2][c2] and A[r2][c2] != A[-1][-1]:
                    cnt += 1

print(cnt)