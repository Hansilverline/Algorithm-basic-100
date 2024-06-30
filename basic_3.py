def solution(data): 
    if not data :
        return 0
    sum = 0
    for i in data : 
        if not(i%3 == 0 or i%5 == 0) :
            sum += i
    return sum

data = [1, 2, 3, 4, 5]

print(solution(data))
