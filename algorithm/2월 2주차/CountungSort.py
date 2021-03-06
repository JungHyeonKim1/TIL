A = [0, 4, 1, 3, 1, 2, 4, 1]
B = [0] * len(A)
C = [0] * 5

def countingSort(A, B, C):
    # 카운팅
    for i in range(len(B)):
        C[A[i]] += 1
    # 누적
    for i in range(1, len(C)):
        C[i] = C[i] + C[i-1]
    # 자기자리 찾기
    for i in range(len(A)-1, -1, -1):
        B[C[A[i]] - 1] = A[i]
        C[A[i]] -= 1

countingSort(A, B, C)
print(B)