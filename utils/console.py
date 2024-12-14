class Console:
    # Codes ANSI pour les couleurs
    RESET = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"

    # Couleurs
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"

    # Couleurs d'arrière-plan
    BACK_BLACK = "\033[40m"
    BACK_RED = "\033[41m"
    BACK_GREEN = "\033[42m"
    BACK_YELLOW = "\033[43m"
    BACK_BLUE = "\033[44m"
    BACK_MAGENTA = "\033[45m"
    BACK_CYAN = "\033[46m"
    BACK_WHITE = "\033[47m"

    # Méthode de succès
    @staticmethod
    def success(message):
        print(f"{Console.GREEN}[Succès]{Console.RESET} {message}")

    # Méthode d'erreur
    @staticmethod
    def error(message):
        print(f"{Console.RED}[Erreur]{Console.RESET} {message}")

    # Méthode de warning
    @staticmethod
    def warning(message):
        print(f"{Console.YELLOW}[Warning]{Console.RESET} {message}")

    # Méthode d'info
    @staticmethod
    def info(message):
        print(f"{Console.CYAN}[Info]{Console.RESET} {message}")

    # Méthode pour afficher un message personnalisé en utilisant le style
    @staticmethod
    def custom(message, color=WHITE):
        print(f"{color}{message}{Console.RESET}")

    # Méthode pour afficher un message en gras
    @staticmethod
    def bold(message):
        print(f"{Console.BOLD}{message}{Console.RESET}")

    # Méthode pour afficher un message souligné
    @staticmethod
    def underline(message):
        print(f"{Console.UNDERLINE}{message}{Console.RESET}")


