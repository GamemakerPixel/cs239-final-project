from model.game_state import GameState, GameStateType
from model.menu_options import TitleMenuOption

_OPTIONS_TO_STATES = {
    TitleMenuOption.PLAY: GameStateType.SELECT_ACTION,
    TitleMenuOption.TUTORIAL: GameStateType.SHOW_TUTORIAL,
    TitleMenuOption.QUIT: GameStateType.QUIT,
}


class Title(GameState):

    def start(self) -> GameStateType | None:
        self._view.show_title()
        
        option = self._view.show_title_menu()

        return _OPTIONS_TO_STATES[option]

