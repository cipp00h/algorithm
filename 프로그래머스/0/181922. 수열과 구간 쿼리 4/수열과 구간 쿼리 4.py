def solution(arr, queries):
    for s, e, k in queries:
        arr[s:e+1] = [arr[i] + (i % k == 0) for i in range(s, e + 1)]
    return arr
