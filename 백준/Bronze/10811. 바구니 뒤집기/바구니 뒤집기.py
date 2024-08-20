N, M = map(int, input().split())
arr = [i for i in range(1, N+1)]

for _ in range(M):
    i, j = map(int, input().split())
    i -= 1
    j -= 1
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1

print(' '.join(map(str, arr)))