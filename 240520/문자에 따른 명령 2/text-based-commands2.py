dirs = input()
x, y = 0, 0
curr_dir = 3

dx = [1,  0, -1, 0]
dy = [0, -1,  0, 1]

for dir_str in dirs:
    if dir_str == 'L':
        curr_dir = (curr_dir-1+4)%4
    elif dir_str == 'R':
        curr_dir = (curr_dir+1)%4
    else:
        x = x + dx[curr_dir]
        y = y + dy[curr_dir]

print(x, y)