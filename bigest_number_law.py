# 문제출처 : 이것이 코딩테스트다
# 문제유형 : 그리디
# 문제번호 : 실전 문제 2
# 문제명 : 큰 수의 법칙

N, M, K = map(int, input().split())
data = list(map(int, input().split()))

data.sort(reverse=True)

result = 0

K_count = 0

if data.count(data[0]) > 1:  # 가장 큰 수가 2개 이상인 경우
    result = data[0] * M
elif data.count(data[0]) == 1:  # 가장 큰 수가 1개인 경우
    while True:
        if M == 0:
            break

        for i in range(K):
            if M == 0:
                break
            result += data[0]
            M -= 1

        result += data[1]
        M -= 1

print(result)

