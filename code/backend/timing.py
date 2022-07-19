"""Import datetime, to get the time and calculate the time till the event """
import datetime


def time_till_format(wait_time: str):
    """calculates the time till an event

    Args:
        wait_time(str): the time, the event happes

    Returns:
        str: time the event in hh:mm:ss"""
    cur_time = str(datetime.datetime.now()).split(" ")[1].split(".")[0]
    wait_time = str(wait_time)

    # get hours, min, sec from format hh:mm:ss
    split_cur_time = cur_time.split(":")
    cur_time_h = split_cur_time[0]
    cur_time_m = split_cur_time[1]
    cur_time_s = split_cur_time[2]

    split_wait_time = wait_time.split(":")
    wait_time_h = split_wait_time[0]
    wait_time_m = split_wait_time[1]
    wait_time_s = split_wait_time[2]

    # converts the time hh:mm:ss in seconds
    cur_time_sec = (((int(cur_time_h) * 60) + int(cur_time_m)) * 60) + int(cur_time_s)
    wait_time_sec = (((int(wait_time_h) * 60) + int(wait_time_m)) * 60) + int(wait_time_s)

    # for the next day = when wait_time < cur_time
    if wait_time_sec < cur_time_sec:
        wait_time_sec += 86400

    # wait_time - current time (in sec) = the time till the event (in sec)
    var_time_till = wait_time_sec - cur_time_sec

    # convert back the seconds in hours, minutes and seconds
    calc_time_till = var_time_till
    time_till_h = calc_time_till // 3600
    calc_time_till = calc_time_till - (time_till_h * 3600)
    time_till_m = calc_time_till // 60
    calc_time_till = calc_time_till - (time_till_m * 60)
    time_till_s = calc_time_till

    # convert back to string, to add a 0,
    #  if there is only one character
    time_till_h = str(time_till_h)
    time_till_m = str(time_till_m)
    time_till_s = str(time_till_s)

    # puts a 0 before the number,
    # if there only is one character
    if len(time_till_h) == 1:
        time_till_h = "0" + time_till_h

    if len(time_till_m) == 1:
        time_till_m = "0" + time_till_m

    if len(time_till_s) == 1:
        time_till_s = "0" + time_till_s

    str_time_till = time_till_h + ":" + time_till_m + ":" + time_till_s
    return str_time_till

def time_till_sec(wait_time: str):
    """calculates the time till an event

    Args:
        wait_time(str): the time, the event happes

    Returns:
        str: time the event in hh:mm:ss"""
    cur_time = str(datetime.datetime.now()).split(" ")[1].split(".")[0]
    wait_time = str(wait_time)

    # get hours, min, sec from format hh:mm:ss
    split_cur_time = cur_time.split(":")
    cur_time_h = split_cur_time[0]
    cur_time_m = split_cur_time[1]
    cur_time_s = split_cur_time[2]

    split_wait_time = wait_time.split(":")
    wait_time_h = split_wait_time[0]
    wait_time_m = split_wait_time[1]
    wait_time_s = split_wait_time[2]

    # converts the time hh:mm:ss in seconds
    cur_time_sec = (((int(cur_time_h) * 60) + int(cur_time_m)) * 60) + int(cur_time_s)
    wait_time_sec = (((int(wait_time_h) * 60) + int(wait_time_m)) * 60) + int(wait_time_s)

    # wait_time - current time (in sec) = the time till the event (in sec)
    var_time_till = wait_time_sec - cur_time_sec

    return var_time_till

def time_in_sec(time: str):
    """converts hh:mm:ss time in seconds

    Args:
        time(str): the time you want to convert

    Returns:
        int: time in seconds"""
    time = str(time)

    split_time = time.split(":")
    time_h = split_time[0]
    time_m = split_time[1]
    time_s = split_time[2]

    time =  (((int(time_h) * 60) + int(time_m)) * 60) + int(time_s)

    return time
