import datetime
import time


def hmm(alpha, beta, *args):
    pass  # print(alpha, beta, *args)


hmm("alpha", "beta", "no")

start_time = "04:42 PM"
week_day = "wEdnEsDaY"
week_day = week_day.capitalize()
# print(week_day)
new_start_time = start_time + " " + week_day
# print(new_start_time)
start_time_struct = time.strptime(new_start_time, "%I:%M %p %A")

duration = "02:23"
dur_lst = duration.split(":")
hr_xtra = float(dur_lst[0])
min_xtra = float(dur_lst[1])
print(dur_lst)
start_time_dt = datetime.fromtimestamp(time.mktime(start_time_struct))
# finish = (start_time_struct.tm_hour,start_time_struct.tm) + timedelta(hours=hr_xtra, minutes=min_xtra)
# print(start_time_struct.tm_hour, start_time_struct.tm_min, start_time_struct.tm_wday)
