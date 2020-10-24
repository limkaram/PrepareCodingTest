# 문제출처 : 프로그래머스
# 문제유형 : 스택/큐
# 문제번호 : 코딩테스트 연습 > 스택/큐 > 주식가격
# 문제명 : 주식가격

from collections import deque

def solution(prices):
    answer = [0] * len(prices)

    for idx in range(len(prices)):
        second = 0
        q = deque(prices[idx+1:])
        for _ in range(len(q)):
            price = q.popleft()
            second += 1
            if prices[idx] > price:
                break
        answer[idx] += second
    return answer


if __name__ == '__main__':
    prices = [1, 2, 3, 2, 3]
    # prices = [4, 3, 2, 1, 1]
    # prices = [1, 1, 1, 1, 1]
    # prices = [1, 1, 1, 1, 1]
    # prices = [10, 9, 8, 7, 6]
    # prices = [2, 2, 3, 2, 3, 1]
    result = solution(prices)
    print(result)