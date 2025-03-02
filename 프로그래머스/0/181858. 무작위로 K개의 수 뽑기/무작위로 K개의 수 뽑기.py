def solution(arr, k):
    result = []
    temp = set()
    
    for n in arr:
        if len(result) == k:
            break
            
        if n not in temp:
            result.append(n)
            temp.add(n)
    
    while len(result) < k:
        result.append(-1)
        
    return result