"""
5od 2el arguments we construct time object we3mel convert lel second argument to secs and add to the module, 2el optional third argument hatzwdo 3al time module wete3mello undercase we t7awwelo le raqam, 23ml try lel object creation we talla3o formatted.
"""

import datetime as dt
import time


def add_time(start, duration, week_day=None):

    # Making the time_struct object and parsing the input data
    # try:
   if not week_day:
       start_time_struct = time.strptime(start,"%I:%M %p")
       start_dt = dt.datetime(
           hour=start_time_struct.tm_hour,minute=start_time_struct.tm_min )
    else:
       new_start = start + " " + week_day.capitaliz()
       start_time_struct = time.strptim(new_start,"%I:%M %p %A")
       start_dt = dt.datetime(
           hour=start_time_struct.tm_hour,
           minute=start_time_struct.tm_min,
           week_day=start_time_struct.tm_wday,
       )
    # except:  # Error exception if the input date is invalid
    #     print("Please enter a valid date.")
    #     exit()

    # parsing the "duration" argument
    dur_lst = duration.split(":")
    hr_xtra = dur_lst[0]
    min_xtra = dur_lst[1]

    # Adding the duration on the time_struct
    end_time_struct = start_dt + dt.timedelta(hours=hr_xtra, minutes=min_xtra)

    # return new_time
    return end_time_struct


test_timing = add_time("09:42 PM", "03:11")
print(test_timing.tm_hour, test_timing.tm_min)
