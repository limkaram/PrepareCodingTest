# 문제출처 : 프로그래머스
# 문제유형 : 정렬
# 문제번호 : 코딩테스트 연습 > 정렬 > K번째 수
# 문제명 : K번째 수

def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command
        temp = array[i-1:j]
        temp.sort()
        answer.append(temp[k-1])
    return answer

if __name__ == '__main__':
    array = [1, 5, 2, 6, 3, 7, 4]
    commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
    solution(array, commands)