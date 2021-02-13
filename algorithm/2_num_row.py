import sys
sys.stdin = open("2_num_row.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    asw = 0
    a = 0
    if len(A) <= len(B):
        for i in range(N):
            for j in range(M):
                a += A[i] * B[i]
                if a > 0:
                    asw = a
                    j += 1

    else:
        for j in range(M):
            for i in range(N):
                a += A[j] * B[j]
                if a > 0:
                    asw = a
                    i += 1

    print("#{} {}".format(tc, asw))
