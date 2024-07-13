def solution(data):
    schedules = []
    for day,dates in data.items() :
        for date in dates :
            converted_date = f'{date[2:]} {day}'
            schedules.append(converted_date)
    return sorted(schedules,reverse=True)[:3]

solution({'월': ['2024-01-01', '2024-01-08', '2024-01-15', '2024-01-22'], '화': ['2024-01-02', '2024-01-09', '2024-01-16'], '수': ['2024-01-03', '2024-01-10'], '목': ['2024-01-04', '2024-01-11', '2024-01-18'], '금': ['2024-01-05', '2024-01-12', '2024-01-19', '2024-01-26']})
