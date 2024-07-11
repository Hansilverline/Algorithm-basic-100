def solution(data) :
    key_list = sorted(data.keys())
    return [data[i] for i in key_list]
  
solution({'AX21': 'Moby Dick', 'BX32': '1984', 'CX14': 'To Kill a Mockingbird'})
