def solution(my_string):
    alpha_dict = {'a', 'e', 'i', 'o', 'u'}
    return ''.join([c for c in my_string if c not in alpha_dict])
