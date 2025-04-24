from model.game_state import GameState, GameStateType
from model.menu_options import GameWonOption

_OPTIONS_TO_STATES = {
    GameWonOption.CONTINUE: GameStateType.SELECT_ACTION,
    GameWonOption.MENU: GameStateType.TITLE,
    GameWonOption.QUIT: GameStateType.QUIT,
}


class GameWon(GameState):
    def start(self) -> GameStateType | None:
        self._view.show_company_status(
            self._data.get_balance(),
            self._data.get_customer_count()
        )
        option = self._view.show_game_won_menu()

        if option == GameWonOption.CONTINUE:
            self._data.enable_endless_mode()
        
        return _OPTIONS_TO_STATES[option]


