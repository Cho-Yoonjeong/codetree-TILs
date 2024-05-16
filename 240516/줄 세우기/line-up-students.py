class User:
    def __init__(self, h, w, num):
        self.h = h
        self.w = w
        self.num = num

N = int(input())
A = []
for i in range(N):
    h, w = map(int, input().split())
    A.append(User(h, w, i+1))

A.sort(key=lambda x: (-x.h, -x.w, x.num))

for user in A:
    print(user.h, user.w, user.num)