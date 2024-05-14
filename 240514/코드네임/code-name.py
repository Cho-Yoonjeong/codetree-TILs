class User:
    def __init__(self, code_name, score):
        self.code_name = code_name
        self.score = score

A = []
for _ in range(5):
    code_name, score = input().split()
    user = User(code_name, int(score))
    A.append(user)

ans_user = A[0] # 가장 낮은 점수인 요원을 저장
for user in A:
    # 지금까지의 최저 점수 > 현유저의 점수
    # 지금까지의 최저 유저를 현유저로 변경
    if ans_user.score > user.score:
        ans_user = user
print(ans_user.code_name, ans_user.score)