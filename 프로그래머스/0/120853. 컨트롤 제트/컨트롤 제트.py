def solution(s):
    result = []
    [result.pop() if i == "Z" else result.append(int(i)) for i in s.split()]
    return sum(result)