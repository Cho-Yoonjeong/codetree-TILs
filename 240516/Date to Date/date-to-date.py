num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

#1/1~m/d
def get_days(m, d):
    days = 0
    for i in range(1, m):
        days += num_of_days[i]
    days += d
    return days

m1, d1, m2, d2 = map(int, input().split())

print(get_days(m2, d2) - get_days(m1, d1) + 1)