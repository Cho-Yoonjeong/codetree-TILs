arr = input().split()
wid = int(arr[0])
leng = int(arr[1])

wid += 8
leng *= 3

print(f"{wid}\n{leng}\n{wid*leng}")