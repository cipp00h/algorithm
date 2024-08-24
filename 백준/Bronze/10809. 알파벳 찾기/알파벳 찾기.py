S = input()

alphabet_list = [i for i in range(97,123)]

for i in alphabet_list:
    if chr(i) in S:
        print(S.index(chr(i)), end=" ")
    else:
        print(-1, end=" ")