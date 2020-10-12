# 문제출처 : 이것이 코딩테스트다
# 문제유형 : 그리디
# 문제번호 : 실전 문제 3
# 문제명 : 숫자 카드 게임

N, M = map(int, input().split())
matrix = []

for i in range(N):
    matrix.append(list(map(int, input().split())))

result = max(map(lambda x: min(x), matrix))

print(result)
