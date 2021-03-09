import sys
sys.stdin = open("미로2.txt", "r")

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def Start():
    for i in range(100):
        for j in range(100):
            if arr[i][j] == 2:
                return i, j

def Bfs(x, y):
    Q.append((x, y))
    visited[x][y] = 1

    while len(Q) != 0:  # Q가 비어있지않으면
        tx, ty = Q.pop(0)  # 시작점 저장(deQueue)
        for i in range(4):
            nx = tx + dx[i]
            ny = ty + dy[i]
            if nx < 0 or nx > 99: continue
            if ny < 0 or ny > 99: continue
            if visited[nx][ny] == 0 and arr[nx][ny] == 0:
                Q.append((nx, ny))
                visited[nx][ny] = 1
            if arr[nx][ny] == 3:
                return 1
    return 0

T = 10
for tc in range(1, T + 1):
    no = int(input())
    arr = [list(map(int, input())) for _ in range(100)]
    sx, sy = Start()
    visited = list([0] * 100 for _ in range(100))
    Q = []
    ans = Bfs(sx, sy)
    print('#{} {}'.format(tc, ans))