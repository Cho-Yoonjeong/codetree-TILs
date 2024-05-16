arr = list(map(int, input().split()))
new_arr = []

for i in range(0, 10):
    if i==0 or i==1:
        new_arr.append(arr[i])
    if i >= 2:
        k = new_arr[i-1] + 2*new_arr[i-2]
        new_arr.append(k)
    
print(*new_arr)