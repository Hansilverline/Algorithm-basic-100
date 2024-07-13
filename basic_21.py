def solution(data):
    if data[1] in data[0] :
        index_ = data[0].index(data[1])
        return index_ 
    else :
        return False
      
solution(([1, 3, 5, 7, 9], 5))
