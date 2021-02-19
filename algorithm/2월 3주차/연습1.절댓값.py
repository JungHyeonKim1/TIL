def cal_abs(a, b):
    if a - b > 0:
        return a - b
    else:
        return b - a

N = 5
arr = [list(map(int, input().split())) for _ in range(5)]
print(arr)

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

sum_value = 0
for y in range(N):
    for x in range(N):
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N: continue
            if ny < 0 or ny >= N: continue
            # if 0<=nx<N and 0<=ny<N:
            sum_value += cal_abs(arr[y][x], arr[ny][nx])

print(sum_value)