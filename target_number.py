# 문제출처 : 프로그래머스
# 문제유형 : 탐욕법(Greedy)
# 문제번호 : 코딩테스트 연습 > 깊이/너비 우선 탐색(DFS, BFS) > 타겟 넘버
# 문제명 : 타겟 넘버


def solution(numbers, target):
    tree = [0]

    for number in numbers:
        sub_tree = []
        for node_num in tree:
            sub_tree.append(node_num + number)
            sub_tree.append(node_num - number)
        tree = sub_tree
    return tree.count(target)


if __name__ == '__main__':
    numbers = [1, 2, 3]
    target = 2
    solution(numbers, target)