"""inporting own backend"""
from backend import open_tab


TEXT = ""
links_to_open = []

wel_text = []
wel_text.append()

# save in txt file for pylint
print("████████╗ █████╗ ██████╗     ███████╗ ██████╗██╗  ██╗███████╗██████╗ ██╗   ██╗██╗     ███████╗██████╗ ")
print("╚══██╔══╝██╔══██╗██╔══██╗    ██╔════╝██╔════╝██║  ██║██╔════╝██╔══██╗██║   ██║██║     ██╔════╝██╔══██╗")
print("   ██║   ███████║██████╔╝    ███████╗██║     ███████║█████╗  ██║  ██║██║   ██║██║     █████╗  ██████╔╝")
print("   ██║   ██╔══██║██╔══██╗    ╚════██║██║     ██╔══██║██╔══╝  ██║  ██║██║   ██║██║     ██╔══╝  ██╔══██╗")
print("   ██║   ██║  ██║██████╔╝    ███████║╚██████╗██║  ██║███████╗██████╔╝╚██████╔╝███████╗███████╗██║  ██║")
print("   ╚═╝   ╚═╝  ╚═╝╚═════╝     ╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝")

while TEXT != "no":
    time = input("Enter time (hours:minutes:seconds): ")
    url = input("Enter url (https://www.google.com): ")
    temp = (time, url)
    links_to_open.append(temp)

    TEXT = input("Do you want to schedule another tab? (yes/no)")

if len(links_to_open) == 1:
    open_tab(temp[1], temp[0])
