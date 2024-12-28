def solution(arr, queries):
    answer = []
    
    for s, e, k in queries:
        found_value = -1
        
        for n in arr[s:e+1]:
            if n > k:
                if found_value == -1 or n < found_value:
                    found_value = n
        
        answer.append(found_value)
    
    return answer
