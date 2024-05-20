dxs = [0, 0, 1, -1]
dys = [1, -1, 0, 0]

N = int(input())
A = [
    list(map(int, input().split()))
    for _ in range(N)
]

answer = 0
for i in range(N):
    for j in range(N):
        cnt = 0
        for dx, dy in zip(dxs, dys):
            x = i + dx
            y = j + dy
            if not(0<=x<N and 0<=y<N):
                continue
            cnt += A[x][y]
        if cnt >= 3:
            answer += 1

print(answer)