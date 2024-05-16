n = int(input())
arr = []
arr.append(1)
arr.append(n)

for i in range(2,100):
    k = arr[i-2] + arr[i-1]
    arr.append(k)
    if arr[i] >= 100:
        break
        
print(*arr)