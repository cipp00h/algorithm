from math import gcd

def solution(numer1, denom1, numer2, denom2):
    denominator = denom1 * denom2
    numerator = (numer1 * denom2) + (numer2 * denom1)
    
    greatest_common_divisor = gcd(numerator, denominator)
    
    return [numerator // greatest_common_divisor, denominator // greatest_common_divisor]