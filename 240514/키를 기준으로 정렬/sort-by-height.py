class Person:
    def __init__(self, name, h, w):
        self.name = name
        self.h = h
        self.w = w

N = int(input())
People = []
for _ in range(N):
    name, h, w = input().split()
    People.append(Person(name, int(h), int(w)))

People.sort(key=lambda x: x.h)
for p in People:
    print(p.name, p.h, p.w)