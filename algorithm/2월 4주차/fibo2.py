'''
memo를 위한 배열을 할당하고, 모두 0으로 초기화 한다
memo[0]을 0으로 memo[1]는 1로 초기화 한다
'''

def fibo(n) :
    # global memo
    if n >= 2 and len(memo) <= n :  # n 보다 크면 이미 값이 구해져 있음.
        memo.append(fibo(n-1) + fibo(n-2))
    return memo[n]

memo = [0, 1]
print(fibo(1000))
# print(memo)

#############################
# memo2= [-1] * 21
# memo2[0] = 0
# memo2[1] = 1
# def fibo2(n):
#     if memo2[n] == -1:
#         memo2[n] = fibo2(n-1) + fibo2(n-2)
#
#     return memo2[n]
# print(fibo2(5))
# print(memo2)