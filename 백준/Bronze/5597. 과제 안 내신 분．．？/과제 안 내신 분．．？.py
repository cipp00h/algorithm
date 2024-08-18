n_list = set(i for i in range(1, 31))
temp_list = set()
for i in range(28):
    temp_list.add(int(input()))

diff = n_list - temp_list
print(min(diff))
print(max(diff))