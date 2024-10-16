def solution(binomial):
    a, op, b = binomial.split()
    answer = {
        '+': int(a) + int(b),
        '-': int(a) - int(b),
        '*': int(a) * int(b)
    }
    return answer[op]
