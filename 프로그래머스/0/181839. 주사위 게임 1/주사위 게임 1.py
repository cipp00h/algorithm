def solution(a, b):
    if a % 2 != b % 2:
        return 2 * (a + b)
    elif a % 2 != 0:
        return a ** 2 + b ** 2
    else:
        return abs(a - b)
