def solution(a, b):
    ab = int(str(a) + str(b))
    double_ab = 2 * a * b
    return max(ab, double_ab)