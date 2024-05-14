class Code:
    def __init__(self, code, color, second):
        self.code = code
        self.color = color
        self.second = second

co, col, sec = input().split()
code1 = Code(co, col, int(sec))

print(f"code : {code1.code}")
print(f"color : {code1.color}")
print(f"second : {code1.second}")