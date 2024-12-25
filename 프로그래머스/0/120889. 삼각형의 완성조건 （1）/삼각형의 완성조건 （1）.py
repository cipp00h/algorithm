def solution(sides):
    a, b, c = sides
    return 1 if a + b > c and a + c > b and b + c > a else 2
