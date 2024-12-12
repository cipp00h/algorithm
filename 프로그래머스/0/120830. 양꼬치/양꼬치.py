def solution(n, k):
    discount = (n // 10) * 2000
    total_price = (n * 12000) + (k * 2000) - discount
    return total_price
