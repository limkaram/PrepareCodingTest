# 문제출처 : 프로그래머스
# 문제유형 : 완전탐색
# 문제번호 : 코딩테스트 연습 > 완전탐색 > 카펫
# 문제명 : 카펫

def solution(brown, yellow):
    answer = []

    # 1. 약수를 통해 가능한 모든 카펫의 경우를 도출
    tiles = brown + yellow
    possible = []

    for i in range(1, tiles+1):
        if tiles % i == 0:
            possible.append([i, tiles // i])  # [가로, 세로]

    # 2. 그 중 가로의 크기는 세로와 같거나 더 크다는 조건 반영하여 경우 축소
    more_possible = []
    for width, height in possible:
        if width >= height and width != 1 and width not in [1, 2] and height not in [1, 2]:
            more_possible.append([width, height])

    # 3. 테두리 격자 갯수와 입력의 brown/내부 격자의 갯수와 입력의 yellow와 같은 것만 추림
    if len(more_possible) == 1:
        answer = more_possible[0]
    elif len(more_possible) > 1:
        for width, height in more_possible:
            surround = (width * 2) + (height * 2) - 4
            inside = (width * height) - surround
            if surround == brown and inside == yellow:
                answer = [width, height]
    # print(answer)

    return answer