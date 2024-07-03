def solution(data):
    sorted_list = sorted(data, key=lambda x: x[1])
    keys = []
    for i in sorted_list:
        keys.append(i[0]) 
    return keys

data = [['A', 3], ['B', 1], ['C', 2]]
solution(data)

#list(map(lambda x : x[0],sorted(data,key = lambda x : x[1]))) 
