OFFSET = 1000

A = [
    [0]*2000
    for _ in range(2000)
]

# A, B -> color:1 / M -> color:0
def cover(color):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            A[x+OFFSET][y+OFFSET] = color

cover(1)    # A
cover(1)    # B
cover(0)    # M

answer = 0
for i in range(2000):
    for j in range(2000):
        answer += A[i][j]

print(answer)