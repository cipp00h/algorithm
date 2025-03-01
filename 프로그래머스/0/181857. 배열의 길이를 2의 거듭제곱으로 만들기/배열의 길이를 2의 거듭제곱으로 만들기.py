def solution(arr):
    len_arr = len(arr)
    
    target_len = 1
    while target_len < len_arr:
        target_len *= 2
    
    if target_len == len_arr:
        return arr
    
    return arr + [0] * (target_len - len_arr)