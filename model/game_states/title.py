from enum import auto, Enum

from model.game_state import GameState, GameStateType
from model.menu_options import TitleMenuOption

class Title(GameState):
    def start(self) -> GameStateType | None:
        self._view.show_title()
        
        option = self._view.show_title_menu()

        print(option)

        return GameStateType.TITLE


