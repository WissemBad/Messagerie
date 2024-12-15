import datetime

class Logger:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"

    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"

    BACK_BLACK = "\033[40m"
    BACK_RED = "\033[41m"
    BACK_GREEN = "\033[42m"
    BACK_YELLOW = "\033[43m"
    BACK_BLUE = "\033[44m"
    BACK_MAGENTA = "\033[45m"
    BACK_CYAN = "\033[46m"
    BACK_WHITE = "\033[47m"

    @staticmethod
    def _get_current_time():
        return datetime.datetime.now().strftime("%H:%M:%S")

    @staticmethod
    def success(message):
        print(f"[{Logger._get_current_time()}] {Logger.GREEN}[Succès]{Logger.RESET} {message}")

    @staticmethod
    def error(message):
        print(f"[{Logger._get_current_time()}] {Logger.RED}[Erreur]{Logger.RESET} {message}")

    @staticmethod
    def warning(message):
        print(f"[{Logger._get_current_time()}] {Logger.YELLOW}[Warning]{Logger.RESET} {message}")

    @staticmethod
    def info(message):
        print(f"[{Logger._get_current_time()}] {Logger.CYAN}[Information]{Logger.RESET} {message}")

    @staticmethod
    def custom(message, color=WHITE):
        print(f"[{Logger._get_current_time()}] {color}{message}{Logger.RESET}")

    @staticmethod
    def bold(message):
        print(f"[{Logger._get_current_time()}] {Logger.BOLD}{message}{Logger.RESET}")

    @staticmethod
    def underline(message):
        print(f"[{Logger._get_current_time()}] {Logger.UNDERLINE}{message}{Logger.RESET}")


