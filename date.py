from datetime import datetime
from colorama import Fore, Style, init

init()

def logsDate():
    now = datetime.now()
    date = now.strftime('%Y-%m-%d %H:%M:%S')
    date = f"{Style.BRIGHT}{date} {Fore.BLUE}LOGS    {Style.RESET_ALL}"
    return date

def errorDate():
    now = datetime.now()
    date = now.strftime('%Y-%m-%d %H:%M:%S')
    date = f"{Style.BRIGHT}{date} {Fore.RED}ERROR   {Style.RESET_ALL}"
    return date
