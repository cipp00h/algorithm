N = int(input())
score = list(map(int, input().split()))
M = max(score)  # 최고점
sum = 0

for n in score:
    sum += n

print(((sum / M) * 100) / N)