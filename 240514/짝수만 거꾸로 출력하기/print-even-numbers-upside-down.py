n = int(input())
arr = list(map(int, input().split()))
cnt = 0
even = []

for elem in arr:
    if elem%2 == 0:
        even.append(elem)
        cnt += 1

for i in range(cnt-1, -1, -1):
    print(even[i], end=" ")