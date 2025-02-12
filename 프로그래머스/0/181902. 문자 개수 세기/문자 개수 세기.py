def solution(my_string):
    count = [0] * 52
    
    for char in my_string:
        if 'A' <= char <= 'Z':
            count[ord(char) - ord('A')] += 1
        elif 'a' <= char <= 'z':
            count[26 + ord(char) - ord('a')] += 1
    
    return count