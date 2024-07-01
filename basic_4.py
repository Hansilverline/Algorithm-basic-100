def solution(data):
    result = 0
    for index,s in enumerate(data) :
        number = int(s.split()[1].replace('개',''))
        result += number * (index+1)
    return result


data = ['쿠키 3개', '쿠키 2개', '쿠키 5개']

print(solution(data))
