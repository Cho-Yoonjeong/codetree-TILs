n = int(input())

class Student:
    def __init__(self, name, sub1, sub2, sub3):
        self.name = name
        self.sub1 = sub1
        self.sub2 = sub2
        self.sub3 = sub3

A = []
for _ in range(n):
    name, *scores = input().split()
    scores = list(map(int, scores))
    A.append(Student(name, *scores))

A.sort(key=lambda x: (x.sub1 + x.sub2 + x.sub3))
for st in A:
    print(st.name, st.sub1, st.sub2, st.sub3)