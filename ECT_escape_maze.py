# 문제출처 : 이것이 코딩테스트다
# 문제유형 : BFS
# 문제번호 : 실전문제 4
# 문제명 : 미로 탈출

import pprint
from collections import deque

def bfs(x, y):
    n, m = map(int, input().split())
    graph = []

    for i in range(n):
        graph.append(list(map(int, input())))

    print(n, m)
    pprint.pprint(graph)
    queue = deque()
    queue.append((x, y))

    # 이동할 방향 정의(상, 하, 좌, 우)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 미로의 범위를 넘어 서는 경우
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            # 벽인 경우
            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[n-1][m-1]

if __name__ == '__main__':
    print(bfs(0, 0))