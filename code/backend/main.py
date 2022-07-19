import webbrowser
import datetime


current_time = str(datetime.datetime.now()).split(" ")[1].split(".")[0]
print(current_time)
link = "www.google.com"

webbrowser.open(link)
