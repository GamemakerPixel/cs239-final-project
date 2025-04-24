from enum import auto, Enum


class TitleMenuOption(Enum):
    PLAY = auto()
    TUTORIAL = auto()
    QUIT = auto()


class ActionMenuOption(Enum):
    CONTINUE = auto()
    RATES = auto()
    VIEW_DATA = auto()
    BUY_DATA = auto()
    QUIT = auto()
