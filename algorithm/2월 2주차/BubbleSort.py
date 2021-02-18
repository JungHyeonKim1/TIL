def BubbleSort(a):  # 안정정렬이다.
    for i in range(len(a)-1, 0, -1):   # i : 4, 3, 2, 1   pass:4
        for j in range(i): # j : 0 1 2 3
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]



# arr = [55, 7, 78, 12, 42]
# BubbleSort(arr)
# print(arr)



'''
55 7 78 12 42
'''

arr = list(map(int, input().split()))

BubbleSort(arr)
print(arr)

# def BubbleSort(a):
#     for i in range(len(a)-1):   # i : 4, 3, 2, 1   pass:4
#         for j in range(len(a)-1): # j : 0 1 2 3
#             if a[j] > a[j+1]:
#                 a[j], a[j+1] = a[j+1], a[j]