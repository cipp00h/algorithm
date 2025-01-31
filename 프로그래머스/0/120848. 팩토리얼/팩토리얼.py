def solution(n):
    i = 1
    f = 1
    
    while f * (i + 1) <= n:
        i += 1
        f *= i
        
    return i