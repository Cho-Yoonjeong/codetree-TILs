A = input()
N = len(A)

cnt = 0
for i in range(N):
    for j in range(i+1, N):
        if A[i] == '(' and A[j] == ')':
            cnt += 1

print(cnt)