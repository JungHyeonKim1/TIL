import sys
sys.stdin = open("종이붙이기.txt", "r")

# 테스트 케이스
T = int(input())
for tc in range(1, T + 1):
    # 입력값 받기
    n = int(input())

    def fibo(n):
        if n < 2:
            return 1
        else:
            return fibo(n - 1) + fibo(n - 2) * 2

    print("#{} {}".format(tc, fibo(n/10)))