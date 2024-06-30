def solution(data):
    sum = 0
    for i in data :
        if i % 2 != 0  :
            sum += i
    return sum

data = [1, 2, 3, 4, 5]

print(solution(data))
