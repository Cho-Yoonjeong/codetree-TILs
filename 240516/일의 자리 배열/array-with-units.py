arr = list(map(int, input().split()))
new_arr = []
new_arr.append(arr[0])
new_arr.append(arr[1])

for i in range(2,10):
    k = (new_arr[i-2] + new_arr[i-1]) % 10
    new_arr.append(k)

print(*new_arr)