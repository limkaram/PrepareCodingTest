# 문제출처 : 프로그래머스
# 문제유형 : 완전탐색
# 문제번호 : 코딩테스트 연습 > 완전탐색 > 소수 찾기
# 문제명 : 소수 찾기

import itertools


def solution(numbers):
    answer = 0
    number_list = [i for i in numbers]

    all_combinations = []
    for i in range(1, len(numbers)+1):
        all_combinations += list(map(lambda x: int(''.join(x)), itertools.permutations(number_list, i)))

    # print(set(all_combinations))
    for i, combination in enumerate(set(all_combinations)):
        division_count = 0
        if combination not in [0, 1]:
            if combination // 10 >= 1 and combination % 2 != 0 and combination % 3 != 0 and combination % 5 != 0 and combination % 7 != 0:
                # print(combination)
                for num in range(2, combination):
                    if combination % num == 0:
                        division_count += 1
                if division_count == 0:
                    answer += 1
            elif combination // 10 == 0:
                if combination in [2, 3, 5, 7]:
                    answer += 1
    # print(answer)
    return answer


if __name__ == '__main__':
    numbers = '17'
    result = solution(numbers)