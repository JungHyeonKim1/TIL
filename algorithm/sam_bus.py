import sys
sys.stdin = open("sam_bus.txt", "r")

T = int(input())
for tc in range(1, T+1):
    # 노선 개수
    N = int(input())
    for tc2 in range(1, N+1):
        # 해당 노선의 정류장 번호(A이상, B이하)
        A, B = map(int, input().split())
    P = int(input())
    for tc3 in range(1, P+1):
        C = int(input())

        asw = []
        for i in range(N):
            for j in range(P):
                if C >= A and C <= B:
                    asw[j] += 1

    print("#{} {}".format(tc, asw))