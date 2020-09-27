# 문제출처 : 백준 온라인 저지
# 문제유형 : 그리드 알고리즘
# 문제번호 : 11047번
# 문제명 : 동전0

N, K = map(int, input().split())

coins = []

for i in range(N):
    coin = int(input())
    coins.append(coin)

coin_count = 0
remain = 0

for coin in reversed(coins):
    if coin <= K:
        coin_count += K // coin
        K %= coin
    elif K == 0:
        break

print(coin_count)

