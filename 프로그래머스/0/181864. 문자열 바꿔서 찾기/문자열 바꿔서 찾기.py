def solution(myString, pat):
    temp = ''.join(['B' if s == 'A' else 'A' for s in myString])
    return 1 if pat in temp else 0