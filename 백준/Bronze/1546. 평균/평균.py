N = int(input())
score_list = list(map(int, input().split()))
max_score = max(score_list)
total_avg = sum(score / max_score * 100 for score in score_list) / N
print(total_avg)