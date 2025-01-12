def solution(my_string, queries):
    list_str = list(my_string)
    
    for s, e in queries:
        list_str[s:e+1] = list_str[s:e+1][::-1]
        
    return ''.join(list_str)