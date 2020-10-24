# 문제출처 : 이것이 코딩테스트다
# 문제유형 : 그리디
# 문제번호 : 유투브 문제
# 문제명 : 곱하기 혹은 더하기


S = input()
result = int(S[0])

for idx in range(1, len(S)):
    if int(S[idx]) <= 1 or result <= 1:
        result += int(S[idx])
    else:
        result *= int(S[idx])

print(result)
