def solution(data):
    def convert_date(date): 
        if '-' in date : 
            dd,mm,yy = date.split('-')
        elif '/' in  date:
            mm,dd,yy = date.split('/')
        else : 
            yy,mm,dd = date.split('.')
        return yy,mm,dd
    converted_dates = [convert_date(date) for date in data]
    sorted_dates = sorted(converted_dates)
    return ['/'.join(date)for date in sorted_dates]
  
solution(['20-01-2024', '12/15/2023', '2022.05.30'])
