# 문제출처 : 이것이 코딩테스트다
# 문제유형 : BFS
# 문제번호 : BFS 예제
# 문제명 : BFS 구현

from collections import deque

def bfs(graph):
    visited = []
    root = 1
    q = deque([root])

    while q:
        n = q.popleft()
        if n not in visited:
            visited.append(n)

        for i in graph[n]:
            if i not in visited:
                q.append(i)

    print(visited)
def main():
    graph = {
        1: [2, 3, 8],
        2: [1, 7],
        3: [1, 4, 5],
        4: [3, 5],
        5: [3, 4],
        6: [7],
        7: [2, 6, 8],
        8: [1, 7]
    }

    bfs(graph)

if __name__ == '__main__':
    main()