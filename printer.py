# 문제출처 : 프로그래머스
# 문제유형 : 스택/큐
# 문제번호 : 코딩테스트 연습 > 스택/큐 > 프린터
# 문제명 : 프린터

from collections import deque


def solution(priorities, location):
    temp = []
    for idx, prior in enumerate(priorities):
        origin_location = idx
        temp.append([prior, origin_location])
    queue = deque(temp)

    complete = []
    max_prior = max(priorities)

    while True:
        if queue[0][0] == max_prior:
            complete.append(queue.popleft())
            if len(queue) == 0:
                break
            else:
                max_prior = max([i[0] for i in queue])
        else:
            queue.append(queue.popleft())
    answer = [idx+1 for idx, value in enumerate(complete) if value[1] == location][0]
    return answer


if __name__ == '__main__':
    priorities = [2, 1, 3, 2, 4, 1, 2]
    location = 0
    result = solution(priorities, location)