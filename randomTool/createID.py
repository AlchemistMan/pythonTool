import time
import random
import datetime

class IDCard:
    def idCard():
        Dis = '120113'
        curr_time = int(time.strftime('%Y'))
        start_time = curr_time - 54
        end_time = curr_time - 21
        year = str(random.randint(start_time, end_time))
        da = datetime.date.today() + datetime.timedelta(days=random.randint(1, 366))
        date = da.strftime('%m%d')
        ex = str(random.randint(100, 300))
        id = Dis + year + date + ex
        i = 0
        count = 0
        weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
        checkcode = {'0': '1', '1': '0', '2': 'X', '3': '9', '4': '8', '5': '7', '6': '6', '7': '5', '8': '4', '9': '3',
                     '10': '2'}
        for i in range(0, len(id)):
            count = count + int(id[i]) * weight[i]
        f = checkcode[str(count % 11)]
        NO = id + f
        return NO
