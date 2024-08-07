N = int(input())
width = N # 문자열의 폭 

for i in range(1, N+1):
    print(('*' * i).rjust(width))