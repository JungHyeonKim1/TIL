# { 1, 2, 3} 부분집합
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = len(arr)
A = [0] * N  # 원소의 포함 여부를 저장


def powerset(n, k, cursum):  # n : 원소의 갯수, k : 현재 depth
    global cnt
    global total
    ########### 가지치기#######################
    if cursum > 10: return
    #########################################
    total += 1
    if n == k:
        # 솔루션구하기
        #합이 10일때 카운트 증가, 출력
        if cursum == 10 :
            cnt += 1
            print(cnt, end= " : ")
            for i in range(n):
                if A[i]:
                    print(arr[i], end=" ")
            print()
    else:
        A[k] = 1
        powerset(n, k + 1, cursum + arr[k])
        A[k] = 0
        powerset(n, k + 1, cursum)

cnt = 0
total = 1
powerset(N, 0, 0)
print(total)
