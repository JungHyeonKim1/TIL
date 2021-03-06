import sys
sys.stdin = open("토너먼트카드게임.txt")
def f(l, r):    # 왼쪽, 오른쪽 인덱스
    # 기본파트
    if l == r:
        return l
    # 유도파트
    else:
        # 아래서 받은 값
        r1 = f(l, (l+r)//2)     # 왼쪽
        r2 = f((l+r)//2+1, r)   # 오른쪽
        # 계산해서 리턴
        if card[r1] == card[r2]:
            return r1
        else:
            if card[r1] == 1 and card[r2] == 2 : # 가위 Vs 바위
                return r2
            elif card[r1] == 1 and card[r2] == 3: # 가위 Vs 보
                return r1
            elif card[r1] == 2 and card[r2] == 1: # 바위 Vs 가위
                return r1
            elif card[r1] == 2 and card[r2] == 3: # 바위 Vs 보
                return r2
            elif card[r1] == 3 and card[r2] == 1: # 보 Vs 가위
                return r2
            elif card[r1] == 3 and card[r2] == 2: # 가위 Vs 보
                return r1

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    card =[0] + list(map(int, input().split()))
    print("#{} {}".format(tc, f(1, N)))

