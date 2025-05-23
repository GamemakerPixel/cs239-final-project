from model.game_state import GameState, GameStateType
from model.menu_options import ActionMenuOption

_OPTIONS_TO_STATES = {
    ActionMenuOption.CONTINUE: GameStateType.DAILY_RESULTS,
    ActionMenuOption.RATES: GameStateType.MANAGE_RATES,
    ActionMenuOption.VIEW_DATA: GameStateType.VIEW_DATA,
    ActionMenuOption.BUY_DATA: GameStateType.BUY_DATA,
    ActionMenuOption.QUIT: GameStateType.QUIT,
}


class SelectAction(GameState):
    def start(self) -> GameStateType | None:
        self._view.show_company_status(
            self._data.get_balance(),
            self._data.get_customer_count()
        )
        
        option = self._view.show_action_menu()

        return _OPTIONS_TO_STATES[option]

