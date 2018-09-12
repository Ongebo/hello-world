def hanoi(n, x, y, z):
    if n == 1:
        print('Move disk', n, 'from', x, 'to', y)
    else:
        hanoi(n - 1, x, z, y)
        print('Move disk', n, 'from', x, 'to', y)
        hanoi(n - 1, z, y, x)

