N, M = map(int, input().split())
basket = [0 for _ in range(N)]

for _ in range(M):
    i, j, k = map(int, input().split())
    for l in range(i-1, j):
        basket[l] = k

print(' '.join(map(str,basket)))