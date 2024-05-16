n = int(input())
arr = list(map(int, input().split()))

min_val = arr[0]
cnt = 0

for elem in arr:
    if min_val > elem:
        min_val = elem
for i in range(n):
    if arr[i] == min_val:
        cnt += 1

print(min_val, cnt)