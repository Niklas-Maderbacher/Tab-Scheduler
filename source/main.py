"""inporting own backend"""
from backend import open_tab
from backend import time_in_sec
from backend import tuple_sort

TEXT = ""
links_to_open = []

# save in txt file for pylint
print("████████╗ █████╗ ██████╗     ███████╗ ██████╗██╗  ██╗███████╗" +
        "██████╗ ██╗   ██╗██╗     ███████╗██████╗ ")
print("╚══██╔══╝██╔══██╗██╔══██╗    ██╔════╝██╔════╝██║  ██║██╔════╝" +
        "██╔══██╗██║   ██║██║     ██╔════╝██╔══██╗")
print("   ██║   ███████║██████╔╝    ███████╗██║     ███████║█████╗  " +
        "██║  ██║██║   ██║██║     █████╗  ██████╔╝")
print("   ██║   ██╔══██║██╔══██╗    ╚════██║██║     ██╔══██║██╔══╝  " +
        "██║  ██║██║   ██║██║     ██╔══╝  ██╔══██╗")
print("   ██║   ██║  ██║██████╔╝    ███████║╚██████╗██║  ██║███████╗" +
        "██████╔╝╚██████╔╝███████╗███████╗██║  ██║")
print("   ╚═╝   ╚═╝  ╚═╝╚═════╝     ╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝" +
        "╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝")


while TEXT != "no":
    time = input("Enter time (hours:minutes:seconds): ")
    url = input("Enter url (https://www.google.com): ")
    temp = (time, url)
    links_to_open.append(temp)

    TEXT = input("Do you want to schedule another tab? (yes/no): ")

if len(links_to_open) == 1:
    open_tab(temp[1], temp[0])

if len(links_to_open) >= 2:
    new_list = []

    for element in links_to_open:
        url = element[1]
        time_sec = time_in_sec(element[0])
        temp = (time_sec, url)
        new_list.append(temp)

    new_list = tuple_sort(new_list)

    print(new_list)
