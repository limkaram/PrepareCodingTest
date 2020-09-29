# 문제출처 : 프로그래머스
# 문제유형 : 정렬
# 문제번호 : 코딩테스트 연습 > 정렬 > 가장 큰 수
# 문제명 : 가장 큰 수

import itertools
import random



def solution(numbers):
    numbers_str = map(str, numbers)
    numbers_max_len = max(map(lambda x: len(x), numbers_str))
    print(numbers_max_len)

    for number in numbers_str:
        if len(number) < numbers_max_len:
            number + number[-1] * (numbers_max_len - len(number))

if __name__ == '__main__':
    numbers = [6, 10, 2, 0]  # tc#1
    # numbers = [3, 30, 34, 5, 9]  # tc#2

    # numbers = []  # tc#3
    # for i in range(1, 100001):
    #     numbers.append(random.randint(0, 1000))
    # print(numbers)
    # print(len(numbers))

    # solution(numbers)
