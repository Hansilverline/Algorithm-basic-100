def solution(data):
    return len(list(filter(lambda x: sum(x)/len(x) >= 80 ,data)))

solution([[92, 85, 97], [30, 21, 60], [90, 99, 98], [0, 0, 0], [81, 80, 88]])
