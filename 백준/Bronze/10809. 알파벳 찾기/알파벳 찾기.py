import string
S = input()
alphabet_list = list(string.ascii_lowercase)
result = [-1] * len(alphabet_list)

for i, c in enumerate(S):
    if result[ord(c) - ord('a')] == -1:
        result[ord(c) - ord('a')] = i

print(' '.join(map(str, result)))