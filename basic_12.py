def solution(data):
    return sorted(data[0],key=lambda x: data[1].get(x.split(' ')[1]))
  
solution([['제주시 A동 한라산길 61', '제주시 B동 백록담길 63', '제주시 C동 사라봉길 31'], {'A동': 63007, 'B동': 63010, 'C동': 63002}])
