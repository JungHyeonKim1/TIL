# ascii to integer
def atoi2(string):
    value = 0
    for i in range(len(string)):
        digit = ord(string[i]) - ord('0')
        value = (value * 10) + digit
    return value

def atoi(string):
    value = 0
    for i in range(len(string)):
        c = string[i]
        if c >= '0' and c <='9':
            digit = ord(c) - ord('0')
        else:
            break
        value = (value * 10) + digit
    return value

a = "123"
print(type(a))
b = atoi2(a)
print(b)
print(type(b))

c = int(a)
print(c)
print(type(c))