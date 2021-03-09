import sys
sys.stdin = open("회전.txt", "r")

def rotate():
    for _ in range(M):
        front = arr.pop(0)
        arr.append(front)

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    rotate()
    front = arr.pop(0)
    print("#{}".format(tc), front)