dirs = input()
x, y = 0, 0
dir_num = 3

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

for dir_str in dirs:
    if dir_str == 'L':
        dir_num = (dir_num-1+4)%4
    elif dir_str == 'R':
        dir_num = (dir_num+1)%4
    else:
        x = x + dx[dir_num]
        y = y + dy[dir_num]

print(x, y)