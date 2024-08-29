N = int(input())
width = 2 * N - 1

for i in range(width):
    if i < N:
        stars = 2 * i + 1
    else:
        stars = 2 * (width - i -1) + 1

    spaces = (width - stars) // 2
    print(' ' * spaces + '*' * stars)