def solution(data) :
    def convert_time(time) : 
        hh, mm, ampm = time.split(' ')[0].split(':')+time.split(' ')[1:]
        if ampm == 'PM' and hh != '12' :
            hh = str(int(hh)+12)
        elif ampm == 'AM' and hh == '12' :
            hh = '00'
        return hh+':'+mm+' '+ampm
    return sorted(data,key=convert_time)


solution(['01:00 PM', '11:30 AM', '12:45 PM', '09:00 AM', '12:00 AM'])
