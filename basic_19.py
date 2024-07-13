def solution(data):
    return [str(type(data[i])).split("'")[1] for i in range(len(data))]

solution([123, 4.56, 'hello', [1, 2, 3], (4, 5), {'a': 1, 'b': 2}])
