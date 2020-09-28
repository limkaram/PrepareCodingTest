# 문제출처 : 프로그래머스
# 문제유형 : 해쉬
# 문제번호 : 코딩테스트 연습-해쉬-1번문제
# 문제명 : 완주하지 못한 선수

def solution(participant, completion):
    answer = ''

    result_dict = {}
    for p_name in participant:
        if p_name not in result_dict.keys():
            result_dict[p_name] = 0
        elif p_name in result_dict.keys():
            result_dict[p_name] += 1

    for c_name in completion:
        result_dict[c_name] -= 1

    for key, value in result_dict.items():
        if value == 0:
            return key


if __name__ == '__main__':
    # test case#1
    participant = ['leo', 'kiki', 'eden']
    completion = ['eden', 'kiki']

    # # test case#2
    # participant = ['marina', 'josipa', 'nikola', 'vinko', 'filipa']
    # completion = 	['josipa', 'filipa', 'marina', 'nikola']

    # # test case#3
    # participant = ['mislav', 'stanko', 'mislav', 'ana']
    # completion = ['stanko', 'ana', 'mislav']

    solution(participant, completion)