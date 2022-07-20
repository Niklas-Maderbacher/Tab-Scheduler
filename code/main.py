# from backend.timing import time_in_sec, time_till_format, time_till_sec


text = ""
links_to_open = []

print("████████╗ █████╗ ██████╗     ███████╗ ██████╗██╗  ██╗███████╗██████╗ ██╗   ██╗██╗     ███████╗██████╗ ")
print("╚══██╔══╝██╔══██╗██╔══██╗    ██╔════╝██╔════╝██║  ██║██╔════╝██╔══██╗██║   ██║██║     ██╔════╝██╔══██╗")
print("   ██║   ███████║██████╔╝    ███████╗██║     ███████║█████╗  ██║  ██║██║   ██║██║     █████╗  ██████╔╝")
print("   ██║   ██╔══██║██╔══██╗    ╚════██║██║     ██╔══██║██╔══╝  ██║  ██║██║   ██║██║     ██╔══╝  ██╔══██╗")
print("   ██║   ██║  ██║██████╔╝    ███████║╚██████╗██║  ██║███████╗██████╔╝╚██████╔╝███████╗███████╗██║  ██║")
print("   ╚═╝   ╚═╝  ╚═╝╚═════╝     ╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝")
                                                                                                    
while text != "no":
    time = input("Enter time (hours:minutes:seconds): ")
    url = input("Enter url (https://www.google.com): ")
    temp = (time, url)
    links_to_open.append(temp)

    text = input("Do you want to schedule another tab? (yes/no)")


