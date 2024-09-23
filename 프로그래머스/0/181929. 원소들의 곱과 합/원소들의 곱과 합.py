import math

def solution(num_list):
    total_sum = sum(num_list)
    total_product = math.prod(num_list)
    
    return 1 if total_product < total_sum ** 2 else 0
