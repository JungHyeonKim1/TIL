import sys
sys.stdin = open("sam_bus.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    # 노선 개수
    N = int(input())

    bus_stop = [0] * (5001)     # '5001'에 주의!!!

    for i in range(N):
        # 해당 노선의 정류장 번호(A이상, B이하)
        A, B = map(int, input().split())

        for j in range(A, B + 1):
            bus_stop[j] += 1

    P = int(input())

    print("#{}".format(tc), end=" ")
    for i in range(P):
        C = int(input())
        print(bus_stop[C], end=" ")
    print()     # 다음 줄로 넘어가라~!