def solution(num_list):
    sum_odd = ''
    sum_even = ''
    
    for n in num_list:
        if n % 2 != 0:
            sum_odd += str(n)
        else:
            sum_even += str(n)
    
    return int(sum_odd) + int(sum_even)
