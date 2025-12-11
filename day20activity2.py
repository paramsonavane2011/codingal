import random, time

def randomDate(startDate, endDate):
    r = random.random()
    format = "%d/%m/%Y"
    start = time.mktime(time.strptime(startDate, format))
    end = time.mktime(time.strptime(endDate, format))
    rtime = start + r * (end - start)
    rdate = time.strftime(format, time.localtime(rtime))
    return rdate

print(randomDate("1/1/2016", "12/12/2018"))