from datetime import datetime, timedelta

# date_today = datetime.now().date()
# cut_time = input("컷시간은?")
# cut_hour = cut_time[:-2]
# cut_min = cut_time[-2:]
# print(cut_hour)
# print(cut_min)
# print(date_today)

cut_time = input("컷시간은?")
date_dt = datetime.strptime(cut_time, '%H%M')
# print(datetime.now().date(), date_dt.time())
cut_time1 = datetime.combine(datetime.now().date(), date_dt.time())
delta = timedelta(hours=4)
print(cut_time1 + delta)