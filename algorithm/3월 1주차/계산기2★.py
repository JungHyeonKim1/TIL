for t in range(10):
    n = int(input())
    string = input()
    arr = list()
    exp = ""

    for token in string:
        if token == "+":
            while arr:
                exp += arr.pop()
            arr.append(token)
        elif token == "*":
            arr.append(token)
        else:
            exp += token
    while arr:
        exp += arr.pop()

    numbers = []
    for token in exp:
        if token == "+":
            n2 = numbers.pop()
            n1 = numbers.pop()
            n = n1 + n2
            numbers.append(n)
        elif token == "*":
            n2 = numbers.pop()
            n1 = numbers.pop()
            n = n1 * n2
            numbers.append(n)
        else:
            numbers.append(int(token))

    print("#{}".format(t + 1), numbers[0])