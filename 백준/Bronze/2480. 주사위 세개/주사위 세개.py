n = list(map(int, input().split()))

x1 = n.count(n[0])
x2=  n.count(n[1])
x3 = n.count(n[2])

if x1 == 3:
    print(10000 + (n[0] * 1000))
elif x1 == 2:
    print(1000 + (n[0] * 100))
elif x2 == 2:
    print(1000 + (n[1] * 100))
else:
    print(max(n) * 100)