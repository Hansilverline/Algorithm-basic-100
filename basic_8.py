def solution(data):
    return sorted(zip(data,data[1:]),key = lambda x : x[1]-x[0])[0]
  
data = [1, 10, 20, 25, 31, 40]
solution(data)
