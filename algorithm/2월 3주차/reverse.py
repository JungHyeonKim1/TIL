def my_reverse(s):
    arr = list(s)
    N = len(arr)
    for i in range(N//2):
        arr[i],arr[N-1-i] = arr[N-1-i],arr[i]

    str = "".join(arr)
    return str

s = "abcd"
s2 = my_reverse(s)
print(s, type(s))
print(s2, type(s2))



# s = "abcd"          # str
# # s = s[::-1]
# arr = list(s)       # str -> list
# arr.reverse()
# s2 = "".join(arr)   # list -> str
#
# print(s, type(s))
# print(s2, type(s2))