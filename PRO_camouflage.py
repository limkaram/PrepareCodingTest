# 문제출처 : 프로그래머스
# 문제유형 : 해시
# 문제번호 : 코딩테스트 연습 > 해시 > 위장
# 문제명 : 위장

def solution(clothes):
    answer = 1
    clothes_dict = {}

    # dict로 변환
    for cloth, kind in clothes:
        if kind not in clothes_dict:
            clothes_dict[kind] = [cloth]
        else:
            clothes_dict[kind].append(cloth)

    # 종류별 옷가지수 + 1 전체 곱
    # +1의 이유는 각 종류별로 아무 것도 안입는 경우도 고려하기 위함
    for kind in clothes_dict:
        answer *= len(clothes_dict[kind]) + 1

    # -1 이유는 +1로 인해 모든 종류를 아무 것도 안입는 경우가 포함되어 해당 경우를 제외 하기 위함
    return answer - 1