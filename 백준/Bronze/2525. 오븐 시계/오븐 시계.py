H, M = map(int, input().split())
C = int(input())

X = M+C

if X >= 60:
    t1 = X // 60
    t2 = 60 * t1

    if (H + t1) > 23:
        print((H+t1) - 24, X-t2)
    else:
        print(H+t1, X-t2)
else:
    print(H, X)