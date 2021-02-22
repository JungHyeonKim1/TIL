import sys

sys.stdin = open("회문_input.txt")

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())

    # arr = [0] * N
    # for i in range(N):
    #     arr[i] = list(input())
    arr = [list(input()) for _ in range(N)]

    # 입력확인
    # for i in arr:
    #     print(i)

    print("#{} ".format(t), end="")

    # 행방향
    for i in range(N):
        for j in range(N - M + 1):
            flag = 1
            for k in range(M // 2):
                if arr[i][j + k] != arr[i][j + M - 1 - k]:      # 인덱스를 서로 아예 바꾸는 것에 주의하자~! 인덱스도 잘 살피기
                    flag = 0
                    break
            if flag == 1:  # 회문이면 출력
                for k in range(M):
                    print("{}".format(arr[i][j + k]), end="")
                print()
    # 열방향
    for i in range(N):
        for j in range(N - M + 1):
            flag = 1
            for k in range(M // 2):
                if arr[j + k][i] != arr[j + M - 1 - k][i]:      # 인덱스를 서로 아예 바꾸는 것에 주의하자~!
                    flag = 0
                    break
            if flag == 1:
                for k in range(M):
                    print("{}".format(arr[j + k][i]), end="")
                print()
