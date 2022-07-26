"""Import datetime, to get the current time"""
import datetime


def current_time():
    """Returns current time in format hh:mm:ss

    Returns:
        str: current time
    """
    return str(datetime.datetime.now()).split(" ")[1].split(".")[0]

def splitting_time(time: str):
    """Splits time (hh:mm:ss) in own variables
    Args:
        time(str): the time to convert

    Returns:
        lst: [hours, minutes, seconds]
    """
    split_time = time.split(":")
    hours = split_time[0]
    minutes = split_time[1]
    seconds = split_time[2]

    return [hours, minutes, seconds]

def convert_to_seconds(time: str):
    """Converts hh:mm:ss time into seconds
    Args:
        time(str): time in format hh:mm:ss to convert in seconds    

    Returns:
        int: time in seconds
    """
    return (((int(splitting_time(time)[0]) * 60) +
             int(splitting_time(time)[1])) * 60) + int(splitting_time(time)[2])

def seconds_till(event_time: str):
    """Calculates, how many seconds it takes to an event
    Args:
        event_time(str): the time, the event is going to happen

    Returns:
        int: time difference between now and the event in seconds
    """
    if convert_to_seconds(event_time) < convert_to_seconds(current_time()):
        return ((convert_to_seconds(event_time) + 86400) -
                 convert_to_seconds(current_time()))

def format_back(time: int):
    """formats time back in format hh:mm:ss
    Args:
        time(int): time in seconds

    Returns:
        string: time in format hh:mm:ss"""
    # convert back the seconds in hours, minutes and seconds
    calc_time_till = time
    hours = calc_time_till // 3600
    calc_time_till = calc_time_till - (hours * 3600)
    minutes = calc_time_till // 60
    calc_time_till = calc_time_till - (minutes * 60)
    seconds = calc_time_till

    # typecast to string
    hours = str(hours)
    minutes = str(minutes)
    seconds = str(seconds)

    # puts a 0 before the number,
    # if there only is one character
    if len(hours) == 1:
        hours = "0" + hours

    if len(minutes) == 1:
        minutes = "0" + minutes

    if len(seconds) == 1:
        seconds = "0" + seconds

    str_time_till = hours + ":" + minutes + ":" + seconds
    return str_time_till
