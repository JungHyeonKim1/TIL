import sys
sys.stdin = open("토너먼트카드게임.txt", "r")

'''
1: 가위
2: 바위
3: 보
'''

def rockscisorpaper(l_idx, r_idx):
    l, r = cards[l_idx - 1], cards[r_idx - 1]
    if l == r:
        return l_idx
    elif l == 1:  # 가위
        if r == 3:
            return l_idx
        elif r == 2:
            return r_idx
    elif l == 2:  # 바위
        if r == 1:
            return l_idx
        elif r == 3:
            return r_idx
    elif l == 3:  # 보
        if r == 2:
            return l_idx
        elif r == 1:
            return r_idx

def cardgame(lo, hi):
    if lo == hi:
        return lo
    else:
        mid = (lo + hi) // 2
        l = cardgame(lo, mid)
        r = cardgame(mid + 1, hi)
        return rockscisorpaper(l, r)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    cards = list(map(int, input().split()))
    print("#{} {}".format(tc, cardgame(1, N)))