def solution(data):
    return all([class_ == type(instance).__name__ for class_,instance in data])
  
solution([('str', 100), ('dict', {'a': 1}), ('tuple', (1, 2, 3))])
