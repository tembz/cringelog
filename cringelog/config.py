from colorama import Fore


def formatter(text: str) -> str:
    return "\033[1m{}\033[0m".format(text)


class Levels:
    DEBUG = 0
    INFO = 10
    WARNING = 30
    ERROR = 40
    CRITICAL = 50


class LevelNames:
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"

class Colors:
    BLACK = Fore.BLACK
    RED = Fore.RED
    GREEN = Fore.GREEN
    YELLOW = Fore.YELLOW
    BLUE = Fore.BLUE
    MAGENTA = Fore.MAGENTA
    CYAN = Fore.CYAN
    WHITE = Fore.WHITE
    
    LIGHTBLACK_EX  = Fore.LIGHTBLACK_EX
    LIGHTRED_EX = Fore.LIGHTRED_EX
    LIGHTGREEN_EX = Fore.LIGHTGREEN_EX
    LIGHTYELLOW_EX = Fore.LIGHTYELLOW_EX
    LIGHTBLUE_EX = Fore.LIGHTBLUE_EX
    LIGHTMAGENTA_EX = Fore.LIGHTMAGENTA_EX
    LIGHTCYAN_EX = Fore.LIGHTCYAN_EX
    LIGHTWHITE_EX = Fore.LIGHTWHITE_EX