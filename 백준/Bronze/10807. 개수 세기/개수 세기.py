N = int(input())
numbers = list(map(int, input().split()))
v = int(input())
count = 0

for i in range(N):
    if v == numbers[i]:
        count += 1

print(count)