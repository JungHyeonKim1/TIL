arr = [[0,1,2,3],
       [4,5,6,7],
       [8,9,10,11]]
# i : 행의 좌표 , n = len(arr)
# j : 열의 좌표 , m = len(arr[0])
N = 3
M = 4

#행우선
for i in range(N):
    for j in range(M):
        print(arr[i][j], end=" ")
    print()
print()

# 행우선 역으로
for i in range(N):
    for j in range(M-1, -1, -1):
        print(arr[i][j], end=" ")
    print()
print()

#열우선
for j in range(M):
    for i in range(N):
        print(arr[i][j], end=" ")
    print()
print()

for i in range(M):
    for j in range(N):
        print(arr[j][i], end=" ")
    print()
print()



#지그재그 순회
for i in range(len(arr)):
    for j in range(len(arr[0])):
        print(arr[i][j+(M-1-2*j) * (i%2)] , end=" ")
    print()
print()

for i in range(N):
    if i % 2 == 0:
        for j in range(M):
            print(arr[i][j], end=" ")
    else:
        for j in range(M-1, -1, -1):
            print(arr[i][j], end=" ")
    print()
print()