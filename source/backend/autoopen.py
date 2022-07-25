"""importing webbrowser for opening tabs in the browser, importing datetime for time check,
   import timing to get the time till an event, importing time to delay the code"""
import webbrowser
import datetime
import time
from backend import timing


def open_tab(website_link: str, time_to_open: str):
    """opens a tab in the standart browser

    Args:
        Website_Link(str): the link to open in the browser
        time_to_open(str): time to open the tab. Format: hh:mm:ss.
                            If None, instantly opens the tab
    """

    current_time = str(datetime.datetime.now()).split(" ")[1].split(".")[0]

    if current_time == time_to_open or time_to_open is None:
        # new=2, a new tab is trying to get opend, instead of opening a new browser window
        # autoraise not working, shouldn't raise the window, but does
        webbrowser.open(website_link, new=2, autoraise=False)

    else:
        # waits so many second, till the current time equals the input time
        time.sleep(int(timing.time_till_sec(time_to_open)))
        webbrowser.open(website_link, new=2, autoraise=False)
