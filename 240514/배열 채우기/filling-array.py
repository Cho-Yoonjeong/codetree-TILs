arr = list(map(int, input().split()))
arr_new = []

for elem in arr:
    if elem == 0:
        break
    arr_new.append(elem)

if 0 in arr:
    for i in range(len(arr)-2, -1, -1):
        print(arr[i], end=" ")
else:
    for i in range(len(arr)-1, -1, -1):
        print(arr[i], end=" ")