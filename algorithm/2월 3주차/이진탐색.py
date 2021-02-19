def binary_search(a, key): # arr, key
    start = 0
    end = len(a) - 1
    while start <= end:
        mid = (start + end)//2
        # mid일때
        if a[mid] == key:
            return (mid, True)
        #key 작을때
        elif a[mid] > key:
            #end를 mid보다 하나 아래로
            end = mid -1
        #key 클때
        #elif a[mid] < key:
        else:
            #start를 mid보다 하나 크게
            start = mid + 1

    return (-1, False)

arr = [2,4,7,9,11,19,23]
key = 22
print(binary_search(arr, key))