arr = list(map(int, input().split()))
cnt = 0

for elem in arr:
    if elem == 0:
        break
    cnt += 1

print(f"{sum(arr[:cnt+1])} {sum(arr[:cnt+1])/cnt:.1f}")