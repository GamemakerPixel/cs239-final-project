from model.game_data import Customer
from model.game_state import GameState, GameStateType


class SetRate(GameState):
    def start(self) -> GameStateType | None:
        customer = self._data.get_selected_customer()
        new_rate = self._view.show_set_rate_menu(customer)

        customer.set_daily_rate(new_rate)

        self._view.show_updated_customer_rate(customer)

        return GameStateType.MANAGE_RATES
