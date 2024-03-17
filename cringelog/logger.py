
from colorama import Fore
from .config import LevelNames, Colors, formatter, Levels
import datetime


class Logger(Levels):

    def __init__(self) -> None:
        self.levels = {
            "DEBUG": [Fore.LIGHTBLUE_EX, 10],
            "INFO": [Fore.LIGHTGREEN_EX, 20],
            "WARNING": [Fore.YELLOW, 30],
            "ERROR": [Fore.RED, 40],
            "CRITICAL": [Fore.RED, 50]
            }

        self.formatresponse = "{level} | {date} | {message}"
        self.dataformat = "%H:%M:%S"
        self.path = None
        self.min_level = 0


    def setColor(self, name: LevelNames, color: Colors):
        self.levels[name] = color

    def setFormat(self, format: str, dataformat: str | None = None):
        '''
        example format: "{date} | {message} | {level}"
        example dataformat: "YYYY-MM-DDTHH:MM:SS"
        available arguments: date, message, level
        '''
        self.formatresponse = format
        if dataformat is not None:
            self.dataformat = dataformat
    
    def setLevel(self, level):
        self.min_level = level

    def clear(self) -> None:
        self.levels = {
            "DEBUG": [Fore.LIGHTBLUE_EX, 10],
            "INFO": [Fore.LIGHTGREEN_EX, 20],
            "WARNING": [Fore.YELLOW, 30],
            "ERROR": [Fore.RED, 40],
            "CRITICAL": [Fore.RED, 50]
            }

        self.formatresponse = "{level} | {date} | {message}"
        self.dataformat = "%H:%M:%S"
        self.path = None
        self.min_level = 0
        
    def log(self, message, level, write):
        date = datetime.datetime.now().strftime(self.dataformat)
        format_message = formatter(message)
        text = self.formatresponse.format(level=level, date=date, message=format_message)
        if self.levels[level][1] >= self.min_level:
            if self.path is not None and write is True:
                print(self.levels[level][0] + text)
                with open(self.path, "a") as file:
                    file.write(f"{self.formatresponse.format(level=level, date=date, message=message)}\n")
                return
            print(self.levels[level][0] + text)
        

    def debug(self, message, write=True):
        self.log(message=message, level="DEBUG", write=write)
    def info(self, message, write=True):
        self.log(message=message, level="INFO", write=write)
    def warning(self, message, write=True):
        self.log(message=message, level="WARNING", write=write)
    def error(self, message, write=True):
        self.log(message=message, level="ERROR", write=write)
    def critical(self, message, write=True):
        self.log(message=message, level="CRITICAL", write=write)