arr = list(map(int, input().split()))
k = arr[0]

for elem in arr:
    if elem==999 or elem==-999:
        break

for elem in arr:
    if elem>k and elem!=999:
        max_val = elem
    if elem<k and elem!=-999:
        min_val = elem

print(max_val, min_val)