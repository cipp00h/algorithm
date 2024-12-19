def solution(money):
    max_americano_cups, remaining_amount = divmod(money, 5500)
    return [max_americano_cups, remaining_amount]
