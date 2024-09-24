def solution(n, control):
    d = {
        'w': 1,
        's': -1,
        'd': 10,
        'a': -10
    }
    
    for s in control:
        n += d.get(s)
        
    return n
