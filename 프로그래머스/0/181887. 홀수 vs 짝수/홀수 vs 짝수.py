def solution(num_list):
    odd_index_sum = sum(num_list[i] for i in range(len(num_list)) if (i + 1) % 2 != 0)
    even_index_sum = sum(num_list[i] for i in range(len(num_list)) if (i + 1) % 2 == 0)
    
    return max(odd_index_sum, even_index_sum)
