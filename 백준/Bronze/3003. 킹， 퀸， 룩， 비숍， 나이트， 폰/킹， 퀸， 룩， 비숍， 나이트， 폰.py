chess_piece = [1, 1, 2, 2, 2, 8]
input_piece = list(map(int, input().split()))

result = [cp - ip for cp, ip in zip(chess_piece, input_piece)]

print(' '.join(map(str, result)))