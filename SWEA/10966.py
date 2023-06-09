import sys
sys.stdin = open('sample_input.txt')
from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())    # N : 세로크기, M : 가로크기
    arr = [input() for _ in range(N)]

    dist = [[987654321] * M for _ in range(N)]    # 방문체크 겸 거리 체크

    Q = deque()

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'W':
                Q.append((i,j))
                dist[i][j] = 0

    while Q:
        r, c = Q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue
            if arr[nr][nc] == 'L' and dist[nr][nc] == 987654321:
                dist[nr][nc] = dist[r][c] + 1
                Q.append((nr, nc))

    ans = 0

    for i in dist:
        for j in i:
            ans += j
    print('#{} {}'.format(tc, ans))