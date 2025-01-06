import collections

def solution(array):
    most_frequency = collections.Counter(array).most_common()
    if len(most_frequency) > 1 and most_frequency[0][1] == most_frequency[1][1]:
        return -1
    return most_frequency[0][0]

