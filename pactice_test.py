# 문제출처 : 프로그래머스
# 문제유형 : 그리디
# 문제번호 : 코딩테스트 연습 > 완전탐색 > 모의고사
# 문제명 : 모의고사

import itertools

def solution(answers):
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    score = [0, 0, 0]

    for s1, s2, s3, answer in zip(itertools.cycle(p1), itertools.cycle(p2), itertools.cycle(p3), answers):
        if answer == s1:
            score[0] += 1
        if answer == s2:
            score[1] += 1
        if answer == s3:
            score[2] += 1
    max_score = max(score)
    answer = [index+1 for index, value in enumerate(score) if value == max_score]
    return answer


if __name__ == '__main__':
    answers = [1, 3, 2, 4, 2]
    result = solution(answers)