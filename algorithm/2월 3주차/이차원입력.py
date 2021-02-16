# arr = [[1,2,3,4],[1,2,3]]
#
# for i in arr:
#     print(i)

# 3 4
# 1 2 3 4
# 5 6 7 8
# 9 1 2 3


# 1번 방법
N, M = map(int, input().split())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))
for i in arr:
    print(i)


# 2번 방법
N, M = map(int, input().split())
arr = [0] * N
for i in range(N):
    arr[i] = (list(map(int, input().split())))
for i in arr:
    print(i)


# 3번 방법
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]   # _ 대신 i 사용 가능
for i in arr:
    print(i)


# 지그재그
Array[i][j + (m-1-2*j) * (i%2)]