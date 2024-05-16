n = int(input())
arr = []
cnt = 0

for i in range(1,11):
    k = n*i
    arr.append(k)

for elem in arr:
    print(elem, end=" ")
    if elem%5 == 0:
        cnt += 1
    if cnt >=2 :
        break