# 문제출처 : 프로그래머스
# 문제유형 : 탐욕법(Greedy)
# 문제번호 : 코딩테스트 연습 > 탐욕법(Greedy) > 단속카메라
# 문제명 : 단속카메라
# 진행 중

def solution(routes):
    answer = 0
    cars_num = len(routes)

    # 1. 차량이 지나가는 path 산출
    temp = []

    for route in routes:
        temp += route
    path = list(range(min(temp), max(temp)+1))

    # 2. 각 지점별 차량 수 count
    path_count_list = []

    for p in path:
        count = 0
        for route in routes:
            if p in range(route[0], route[1]+1):
                count += 1
        path_count_list.append(count)
    print(path_count_list)

    # 3. 최대의 수가 유지되는 마지막 지점만 카메라를 설치
    max_count = max(path_count_list)

    if len(set(path_count_list)) == 1:
        if 1 in set(path_count_list):  # 모든 차량의 경로가 겹치지 않는 경우
            camera_count = cars_num
            answer = camera_count
        elif cars_num in set(path_count_list):  # 모든 차량의 경로가 겹치는 경우
            camera_count = 1
            answer = camera_count
        elif max_count in set(path_count_list):  #
    elif
    else:
        for index, value in enumerate(path_count_list):



if __name__ == '__main__':
    routes = [[-20, 15], [-14, -5], [-18, -13], [-5, -3]]
    solution(routes)