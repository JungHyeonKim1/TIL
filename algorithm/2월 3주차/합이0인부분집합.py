'''
-3 3 -9 6 7 -6 1 5 4 -2
'''
arr = list(map(int, input().split()))
n = len(arr)
cnt = 0
for i in range(1<<n): # 2^n     0 ~ 7
    sum = 0
    for j in range(n): # 0 ~ 2
        if i & (1 << j):    # 0이 아닌 경우
            sum += arr[j]
    if sum == 0:
        cnt += 1
        for j in range(n):  # 0 ~ 2
            if i & (1 << j):
                print(arr[j], end = " ")

        print()     # 들여쓰기 조심~!~!~!!!!!
print("cnt=", cnt)