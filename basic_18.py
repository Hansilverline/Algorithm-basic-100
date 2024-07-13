def solution(data):
    update_list = []
    for date,temp in data.items():
        converted_date = f'{date[2:]}: {temp}'
        update_list.append(converted_date)
    return sorted(update_list,key=lambda x :x[-2:],reverse=True)[:3]
  
solution({'2024-01-01': 15, '2024-01-02': 17, '2024-01-03': 16, '2024-01-04': 20, '2024-01-05': 19, '2024-01-06': 21, '2024-01-07': 18})
