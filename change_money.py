# 문제출처 : 이것이 코딩테스트다
# 문제유형 : 그리디
# 문제번호 : 예제 31
# 문제명 : 거스름돈

def solution(n):
    coins = [500, 100, 50, 10]
    total_coin = 0

    for coin in coins:
        total_coin += n // coin
        n %= coin
        if n == 0:
            break
    return total_coin


if __name__ == '__main__':
    n = int(input())
    result = solution(n)
    print(result)