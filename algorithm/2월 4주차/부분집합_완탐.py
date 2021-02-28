# { 1, 2, 3} 부분집합
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = len(arr)
A = [0] * N  # 원소의 포함 여부를 저장


def powerset(n, k):  # n : 원소의 갯수, k : 현재 depth
    # 가지치기
    global cnt
    global total
    total += 1
    if n == k:
        # 솔루션구하기
        sum = 0
        # 합구하기
        for i in range(n):
            if A[i]:
               sum += arr[i]
        #합이 10일때 카운트 증가, 출력
        if sum == 10 :
            cnt += 1
            print(cnt, end= " : ")
            for i in range(n):
                if A[i]:
                    print(arr[i], end=" ")
            print()
    else:
        A[k] = 1
        powerset(n, k + 1)
        A[k] = 0
        powerset(n, k + 1)

cnt = 0
total = 1
powerset(N, 0)
print(total)
