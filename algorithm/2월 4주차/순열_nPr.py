# nPr
def perm(n, k):  # 원소의 갯수, k:현재 뎁스
    if R == k:   # n -> R
        print(t)
    else:
        for i in range(n):
            if visited[i]: continue
            t[k] = arr[i]
            visited[i] = 1
            perm(n,k+1)
            visited[i] = 0


arr = [1,2,3]
N = len(arr)
R = 2
t = [0] * R   # 원소의 순서를 저장
visited = [0] * N
perm(N, 0)