def solution(arr):
    x = 0
    
    while True:
        updated_arr = [(num // 2 if num >= 50 and num % 2 == 0 else 
                 num * 2 + 1 if num < 50 and num % 2 == 1 else num) 
                for num in arr]
        
        if arr == updated_arr:
            return x
        
        arr = updated_arr
        x += 1
