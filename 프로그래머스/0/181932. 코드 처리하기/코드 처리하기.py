def solution(code):
    mode = 0
    ret = []
    
    for idx, ch in enumerate(code):
        if ch == "1":
            mode = 1 - mode
        elif (mode == 0 and idx % 2 == 0) or (mode == 1 and idx % 2 != 0):
            ret.append(ch)
    
    return ''.join(ret) if ret else "EMPTY"
