# 문제출처 : 프로그래머스
# 문제유형 : 그리디
# 문제번호 : 코딩테스트 연습 > 탐욕법(Greedy) > 체육복
# 문제명 : 체육복

def solution(n, lost, reserve):
    answer = 0
    clothes_by_student = {}

    # 초기 체육복 갯수 셋팅
    for i in range(1, n+1):
        clothes_by_student[i] = 1

    for i in lost:
        clothes_by_student[i] -= 1

    for i in reserve:
        clothes_by_student[i] += 1

    for i in clothes_by_student:
        posterior = i + 1
        anterior = i - 1

        if posterior > len(clothes_by_student):
            if clothes_by_student[anterior] == 0 and clothes_by_student[i] == 2:
                clothes_by_student[anterior] += 1
                clothes_by_student[i] -= 1
            elif clothes_by_student[anterior] == 2 and clothes_by_student[i] == 0:
                clothes_by_student[anterior] -= 1
                clothes_by_student[i] += 1
        else:
            if clothes_by_student[i] == 2 and clothes_by_student[posterior] == 0:
                clothes_by_student[i] -= 1
                clothes_by_student[posterior] += 1
            elif clothes_by_student[i] == 0 and clothes_by_student[posterior] == 2:
                clothes_by_student[posterior] -= 1
                clothes_by_student[i] += 1

    answer = len([i for i in clothes_by_student.keys() if clothes_by_student[i] >= 1])
    return answer

if __name__ == '__main__':
    n = 2
    lost = [1, 2]
    reserve = [1, 2]

    result = solution(n, lost, reserve)
    print(result)