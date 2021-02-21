def itoa1(num):
    arr =[]

    while num:
        y = num % 10
        num //= 10
        arr.append(y)

    arr.reverse()
    return arr

def my_reverse(s):
    arr = list(s)
    N = len(arr)
    for i in range(N//2):
        arr[i],arr[N-1-i] = arr[N-1-i],arr[i]

    str = "".join(arr)
    return str

def itoa2(num):  # str()
    arr =[]

    while num:
        y = num % 10
        num //= 10
        arr.append(chr(y + ord('0')))

    str = my_reverse(arr)
    return str

x = 123
arr = itoa1(x)
print(arr, type(arr))
str1 = itoa2(x)
print(str1, type(str1))
s = str(x)
print(s, type(str1))