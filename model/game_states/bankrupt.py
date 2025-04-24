from model.game_state import GameState, GameStateType
from model.menu_options import BankruptOption

_OPTIONS_TO_STATES = {
    BankruptOption.MENU: GameStateType.TITLE,
    BankruptOption.QUIT: GameStateType.QUIT,
}


class Bankrupt(GameState):
    def start(self) -> GameStateType | None:
        self._view.show_company_status(
            self._data.get_balance(),
            self._data.get_customer_count()
        )
        option = self._view.show_bankrupt_menu()
        
        return _OPTIONS_TO_STATES[option]

