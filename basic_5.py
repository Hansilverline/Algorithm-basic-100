def solution(data):
    if not data : 
        return 0
    return ''.join(map(str,data)).count('1')

data = [1, 11, 111, 1111]
solution(data)
