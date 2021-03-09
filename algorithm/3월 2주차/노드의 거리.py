import sys
sys.stdin = open("노드의 거리.txt", "r")

# bfs를 실행할 함수
def bfs(default, cnt, goal):
    global result
    next_def = []

    # 현재 큐에 원소가 없을 때까지 진행
    while len(default):
        node = default.pop(0)
        # 끝점에 도달한 경우 종료
        if node == goal:
            result = cnt
            return

        # 현재 노드에서 방문을 안한 노드 중 갈 수 있는 노드를 다음 큐에 추가
        for i in range(1, V + 1):
            if visited[i] == 0 and arr[node][i] == 1:
                visited[i] = 1
                next_def.append(i)

    # 다음에 실행할 큐에 원소가 없을 경우 종료
    if len(next_def) == 0:
        return
    # 원소가 있으면 bfs 다시 실행
    else:
        bfs(next_def, cnt + 1, goal)


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    # 간선 정보를 저장할 이차원 배열
    arr = [[0 for _ in range(V + 1)] for _ in range(V + 1)]
    for _ in range(E):
        x, y = map(int, input().split())
        arr[y][x] = 1
        arr[x][y] = 1
    S, G = map(int, input().split())

    # 노드 방문 기록을 저장할 배열
    visited = [0] * (V + 1)
    result = 0
    # 초기값 정보 정리
    default = [S]
    visited[S] = 1
    bfs(default, 0, G)

    print('#{} {}'.format(tc, result))