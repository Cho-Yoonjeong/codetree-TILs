import sys

n = int(input())
arr = list(map(int, input().split()))

min_dist = sys.maxsize      #부호있는 64비트 기준 가장 큰 값

for i in range(n):
    dist = 0
    for j in range(n):
        dist += abs(i-j) * arr[j]
    min_dist = min(min_dist, dist)

print(min_dist)