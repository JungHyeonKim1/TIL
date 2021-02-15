import sys
sys.stdin = open("소인수분해.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    prime = [2, 3, 5, 7, 11]

    cnt = [0] * 5

    for i in range(len(prime)):
        while N % prime[i] ==0:     # while 쓰는 걸 잘 생각할 수 있어야 한다!
            cnt[i] += 1
            N //= prime[i]

    print("#{} {}".format(tc, " ".join(map(str, cnt))))