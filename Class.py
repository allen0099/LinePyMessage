from datetime import *


class COLOR:
    BLACK = '\033[30m'
    RED = '\033[31m'
    LINE = '\033[32m'
    YELLOW = '\033[33m'
    TELEGRAM = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    BRIGHT_BLACK = '\033[90m'
    FAIL = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    WARNING = '\033[93m'
    SENDER = '\033[94m'
    READ = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    BRIGHT_WHITE = '\033[97m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class TELEGRAM:
    allen0099 = '184805205'
    group = '-1001173035579'


def telegram_log(text):
    print(COLOR.TELEGRAM + "[%s] [TELEGRAM]" % str(datetime.now()) + COLOR.END + " %s" % text)


def line_log(text):
    print(COLOR.LINE + "[%s] [LINE]" % str(datetime.now()) + COLOR.END + " %s" % text)
