class Spy:
    def __init__(self, secret_code, meeting_point, time):
        self.s = secret_code
        self.m = meeting_point
        self.t = time

sc, mp, t = input().split()
spy = Spy(sc, mp, int(t))

print("secret code :", spy.s)
print("meeting point :", spy.m)
print("time :", spy.t)