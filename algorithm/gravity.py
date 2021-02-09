'''
9
7 4 2 0 0 6 0 7 0
'''
n = int(input())
arr = list(map(int, input().split()))
result = 0

for i in range(len(arr)) :
    maxHeight = len(arr) - i - 1
    for j in range(i+1, len(arr)):
        if arr[i] <= arr[j]:
            maxHeight -= 1
    # 최대값 유지?
    if result < maxHeight:
        result = maxHeight

print(result)