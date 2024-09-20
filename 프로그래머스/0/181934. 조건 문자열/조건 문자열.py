def solution(ineq, eq, n, m):
    d = {
        ">=": n >= m,
        "<=": n <= m,
        ">!": n > m,
        "<!": n < m
    }
    
    return 1 if d.get(ineq + eq, False) else 0
    