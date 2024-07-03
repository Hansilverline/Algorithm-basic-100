def solution(data):
    return sorted(data,key=lambda x : x['수'],reverse=True)[0]['이름']
  
data = [{'이름': 'A', '국': 30, '영': 20, '수': 85}, {'이름': 'B', '국': 95, '영': 98, '수': 10}]
solution(data)
