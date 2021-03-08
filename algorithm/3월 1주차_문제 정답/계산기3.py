import sys
sys.stdin = open("계산기3.txt")

def priority(c):
    if c == '(':
        return 0
    elif c == '+' or c == '-':
        return 1
    elif c == '*' or c == '/':
        return 2


def infix_to_postfix(infix):
    # 중위식 스캔
    stack = []
    rst_str = []
    for i in range(len(infix)):
        # 피연산자 -> 문자열 저장
        if '0' <= infix[i] <= '9':
            rst_str.append(infix[i])
        # 연산자
        else:
            # ( 는 푸쉬
            if infix[i] == '(':
                stack.append(infix[i])
            # ) 는 ( 나올때까지 pop -> 문자열
            elif infix[i] == ')':
                while stack[-1] != '(':
                    rst_str.append(stack.pop())
                stack.pop()
            # 사직연산자
            else:
                if len(stack) != 0:
                    # 중위식문자(토큰) <= stack[-1] : push
                    while priority(infix[i]) <= priority(stack[-1]):
                        # else: 토큰보다 우선순위 낮은 연산자 나올때까지 pop
                        rst_str.append(stack.pop())
                        if len(stack) == 0: break  # 비어있냐?
                # stack이 비어있거나 우선순위가 더 높으면
                stack.append(infix[i])
    while len(stack) != 0:
        rst_str.append(stack.pop())
    return "".join(rst_str)  # list -> str


def calc(postfix):
    stack = []
    for i in range(len(postfix)):
        if '0' <= postfix[i] <= '9':
            stack.append(int(postfix[i]))
        elif postfix[i] == '+':
            b = stack.pop()
            a = stack.pop()
            stack.append(a + b)
        elif postfix[i] == '-':
            b = stack.pop()
            a = stack.pop()
            stack.append(a - b)
        elif postfix[i] == '*':
            b = stack.pop()
            a = stack.pop()
            stack.append(a * b)
        elif postfix[i] == '//':
            b = stack.pop()
            a = stack.pop()
            stack.append(a // b)
    return stack.pop()


T = 10
for tc in range(1, 1 + T):
    N = int(input())  # 문자열의 크기
    infix = input()  # 중위식
    postfix = infix_to_postfix(infix)  # 후위식
    print("#{} {}".format(tc, calc(postfix)))