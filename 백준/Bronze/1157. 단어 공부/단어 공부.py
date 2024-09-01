Alphabet = input()
Alphabet_set = set(Alphabet.lower())

d = dict()

for i in Alphabet_set:
    d[i] = Alphabet.lower().count(i)

# 가장 많이 사용된 알파벳 리스트    
max_alphabet_list = [k for k,v in d.items() if max(d.values()) == v]
    
if len(max_alphabet_list) > 1:
    print("?")
else:
    print(max_alphabet_list[0].upper())