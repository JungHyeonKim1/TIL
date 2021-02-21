def bruteForce1(t, p):
    i = 0 #t의 인덱스
    j = 0 #p의 인덱스
    M = len(p) #찾을 패턴의 길이
    N = len(t) #전체 텍스트의 길이
    while j < M and i < N:
        if t[i] != p[j]:
            i = i - j
            j = -1
        i = i + 1
        j = j + 1
    if j == M : return i - M #검색 성공
    else : return -1         #검색 실패

def bruteForce2(t, p):
    N = len(t)
    M = len(p)
    for i in range(N - M + 1):
        cnt =0
        for j in range(M):
            if t[i+j] == p[j]:
                cnt += 1
            else:
                break

        if cnt == M:
            return i
    return -1


t = "a pattern matching algorithm"
p = "rithm"
print("{}".format(bruteForce1(t, p)))
print("{}".format(bruteForce2(t, p)))
print(t.find(p))