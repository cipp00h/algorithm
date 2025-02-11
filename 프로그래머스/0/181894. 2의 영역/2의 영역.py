def solution(arr):
    indices = [idx for idx, num in enumerate(arr) if num == 2]
    return [-1] if not indices else arr[indices[0]:indices[-1] + 1]

