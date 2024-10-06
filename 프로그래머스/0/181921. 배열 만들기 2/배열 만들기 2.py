def solution(l, r):
    answer = []
    for n in range(l, r+1):
        if all(c in '05' for c in str(n)):
            answer.append(n)
    
    if not answer:
        return [-1] 
    
    return answer
