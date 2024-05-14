class Student:
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

N = int(input())
A = []
for _ in range(N):
    name, *scores = input().split()
    scores = list(map(int, scores))
    A.append(Student(name, *scores))

A.sort(key=lambda x: (-x.kor, -x.eng, -x.math))
for st in A:
    print(st.name, st.kor, st.eng, st.math)