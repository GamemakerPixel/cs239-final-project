from abc import ABC, abstractmethod
from enum import auto, Enum

from model.game_data import GameData
from model.view import View


class GameStateType(Enum):
    TITLE = auto()
    SHOW_TUTORIAL = auto()
    QUIT = auto()
    SELECT_ACTION = auto()
    MANAGE_RATES = auto()
    SET_RATE = auto()
    VIEW_DATA = auto()
    BUY_DATA = auto()
    DAILY_RESULTS = auto()
    GAME_WON = auto()
    BANKRUPT = auto()


class GameState(ABC):
    def __init__(self, view: View, data: GameData):
        self._view = view
        self._data = data

    # Return None when the game should end.
    @abstractmethod
    def start(self) -> GameStateType | None:
        pass
