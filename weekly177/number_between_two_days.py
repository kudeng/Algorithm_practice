from datetime import date
date1 = '2019-06-29'
date2 ='2019-06-30'
info1 = date1.split('-')
info2 = date2.split('-')

day1 = date(int(info1[0]), int(info1[1]), int(info1[2]))
day2 = date(int(info2[0]), int(info2[1]), int(info2[2]))
print((day2- day1).days)