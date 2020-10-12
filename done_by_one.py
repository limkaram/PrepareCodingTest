# 문제출처 : 이것이 코딩테스트다
# 문제유형 : 그리디
# 문제번호 : 실전 문제 4
# 문제명 : 1이 될 때까지

result = 0

N, K = map(int, input().split())

while True:
    if N == 1:
        break
    if N % K == 0:
        N //= K
    elif N % K != 0:
        N -= 1
    result += 1

print(result)