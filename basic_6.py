def solution(data):
    if not data : 
        return 0
    return sum(map(int,filter(str.isdigit,data)))

data = '1hel2lo3'
solution(data)
