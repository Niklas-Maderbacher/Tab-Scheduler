"""inporting own backend"""
from backend import open_tab
from backend import convert_to_seconds, format_back
from backend import tuple_sort

TEXT = "yes"
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


while TEXT == "yes":
    url = input("Enter url (https://www.google.com): ")
    time = input("Enter time (hours:minutes:seconds): ")

    temp = (time, url)
    links_to_open.append(temp)

    TEXT = input("Do you want to schedule another tab? (yes/no): ")

if len(links_to_open) == 1:
    open_tab(temp[1], temp[0])

if len(links_to_open) >= 2:
    new_list = []

    for element in links_to_open:
        url = element[1]
        time_sec = convert_to_seconds(element[0])
        temp = (time_sec, url)
        new_list.append(temp)

    new_list = tuple_sort(new_list)

    for schedule in new_list:
        open_tab(schedule[1], format_back(schedule[0]))
