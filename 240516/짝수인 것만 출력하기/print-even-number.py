n = int(input())
arr = list(map(int, input().split()))

new_arr = [elem for elem in arr if elem%2==0]
print(*new_arr)