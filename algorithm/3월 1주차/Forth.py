import sys
sys.stdin = open("Forth.txt", "r")

T = int(input())
for tc in range(1, T+1):
    arr = list(input().split())
    result_list = []
    task_list = ['+', '-', '*', '/']
    result = ''
    for s in arr:
        if s in task_list:
            if len(result_list) == 1:
                result = 'error'
                break
            a = int(result_list.pop())
            b = int(result_list.pop())
            if s == '+':
                temp = b + a
            elif s == '-':
                temp = b - a
            elif s == '*':
                temp = b * a
            elif s == '/':
                temp = b // a
            result_list.append(str(temp))
        elif s == '.':
            if len(result_list) == 1:
                result = result_list.pop()
            else:
                result = 'error'
                break
        else:
            result_list.append(s)
    print('#{} {}'.format(tc, result))