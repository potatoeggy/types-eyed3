import typing
from . import formatSize as formatSize, formatTime as formatTime
from _typeshed import Incomplete

class AnsiCodes:
    def __init__(self, codes) -> None: ...
    def __getattribute__(self, name): ...
    def __getitem__(self, name): ...
    @classmethod
    def init(cls, allow_colors) -> None: ...

class AnsiFore:
    GREY: int
    RED: int
    GREEN: int
    YELLOW: int
    BLUE: int
    MAGENTA: int
    CYAN: int
    WHITE: int
    RESET: int

class AnsiBack:
    GREY: int
    RED: int
    GREEN: int
    YELLOW: int
    BLUE: int
    MAGENTA: int
    CYAN: int
    WHITE: int
    RESET: int

class AnsiStyle:
    RESET_ALL: int
    BRIGHT: int
    RESET_BRIGHT: int
    DIM: int
    RESET_DIM = RESET_BRIGHT
    ITALICS: int
    RESET_ITALICS: int
    UNDERLINE: int
    RESET_UNDERLINE: int
    BLINK_SLOW: int
    RESET_BLINK_SLOW: int
    BLINK_FAST: int
    RESET_BLINK_FAST: int
    INVERSE: int
    RESET_INVERSE: int
    STRIKE_THRU: int
    RESET_STRIKE_THRU: int

Fore: Incomplete
Back: Incomplete
Style: Incomplete

def ERROR_COLOR(): ...
def WARNING_COLOR(): ...
def HEADER_COLOR(): ...

class Spinner:
    def __init__(self, msg, file: Incomplete | None = None, step: int = 1, chars: Incomplete | None = None, use_unicode: bool = True, print_done: bool = True) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: types.TracebackType | None) -> None: ...

class ProgressBar:
    def __init__(self, total_or_items: int | typing.Sequence, file: Incomplete | None = None) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: types.TracebackType | None) -> None: ...
    def __iter__(self): ...
    def __next__(self): ...
    def update(self, value: Incomplete | None = None) -> None: ...
    @classmethod
    def map(cls, function, items, multiprocess: bool = False, file: Incomplete | None = None): ...

def printMsg(s) -> None: ...
def printError(s) -> None: ...
def printWarning(s) -> None: ...
def printHeader(s) -> None: ...
def boldText(s, c: Incomplete | None = None): ...
def formatText(s, b: bool = False, c: Incomplete | None = None): ...
def cformat(msg, fg, bg: Incomplete | None = None, styles: Incomplete | None = None): ...
def getTtySize(fd=..., check_tty: bool = True): ...
def cprint(msg, fg, bg: Incomplete | None = None, styles: Incomplete | None = None, file=...) -> None: ...
