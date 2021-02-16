# bit = [0,0,0,0]
#
# for i in range(2):
#     bit[0] = i
#     for j in range(2):
#         bit[1] = j
#         for k in range(2):
#             bit[2] = k
#             for l in range(2):
#                 bit[3] = l
#                 print(*bit)

arr = [1, 2, 3]
n = len(arr)
for i in range(1<<n): # 2^n     0 ~ 7
    for j in range(n): # 0 ~ 2
        if i & (1 << j):    # 0이 아닌 경우
            print(arr[j], end = " ")

    print()     # 각각 줄 띄우기