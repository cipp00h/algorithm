def solution(rank, attendance):
    students = []
    for i, r in enumerate(rank):
        if attendance[i]:
            students.append((r, i))
    
    students.sort()
    
    a, b, c = students[0][1], students[1][1], students[2][1]
    
    return 10000 * a + 100 * b + c