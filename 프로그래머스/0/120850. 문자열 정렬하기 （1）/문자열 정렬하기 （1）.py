def solution(my_string):
    result = [int(c) for c in my_string if c.isdigit()]
    return sorted(result)