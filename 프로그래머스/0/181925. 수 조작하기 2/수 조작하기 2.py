def solution(numLog):
    d = {
        1: 'w',
        -1: 's',
        10: 'd',
        -10: 'a'
    }
    
    answer = []
    
    for i in range(1, len(numLog)):
        diff = numLog[i] - numLog[i - 1]
        answer.append(d[diff])
    
    return ''.join(answer)
