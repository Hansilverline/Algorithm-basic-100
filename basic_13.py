def solution(data):
    books, publish_years = data
    return sorted(data[0],key= lambda book : (publish_years[book],book))

solution([['Moby Dick', 'To Kill a Mockingbird', '1984'], {'Moby Dick': 1851, 'To Kill a Mockingbird': 1960, '1984': 1949}])
