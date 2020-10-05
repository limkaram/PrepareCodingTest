# 문제출처 : 프로그래머스
# 문제유형 : 스택/큐
# 문제번호 : 코딩테스트 연습 > 스택/큐 > 다리를 지나는 트럭
# 문제명 : 다리를 지나는 트럭

from collections import deque


def solution(bridge_length, weight, truck_weights):
    on_bridge = deque([])
    sec = 0
    complete = []
    bridage_idx = 0

    for idx, wait_t in enumerate(truck_weights):
        if sum(on_bridge) + wait_t <= weight:
            on_bridge.appendleft(wait_t)
        elif sum(on_bridge) + wait_t > weight:
            complete.append(on_bridge.pop())
            sec += bridge_length
            on_bridge.appendleft(wait_t)


if __name__ == '__main__':
    bridge_length = 3
    weight = 10
    truck_weights = [7, 4, 5, 6]

    result = solution(bridge_length, weight, truck_weights)



