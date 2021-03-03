import sys
sys.stdin = open("반복문자 지우기.txt", "r")

# 테스트 케이스
T = int(input())
for tc in range(1, T+1):
    # 입력값 받기
    _str = list(input())

    # 남은 문자열의 길이, 없으면 0을 출력
    N = len(_str)
    stack = []
    for i in range(N):
        # stack이 비었거나, 스택의 마지막 값이 데이터 내 값과 같지 않은 경우
        # => stack에 저장(append)
        if not stack or stack[-1] != _str[i]:
            stack.append(_str[i])
        # stack에 값이 있고, 스택의 마지막 값과 데이터 내 값과 같은 경우
        # => stack에서 제거(pop)
        elif stack and stack[-1] == _str[i]:
            stack.pop()

    print("#{} {}".format(tc, len(stack)))