while True:
    try:
        num = str(input())
        n = 0
        if num.isnumeric():
            n = int(num)
            if n == 0:
                print('vai ter copa!')
            else:
                print('vai ter duas!')
    except EOFError:
        break