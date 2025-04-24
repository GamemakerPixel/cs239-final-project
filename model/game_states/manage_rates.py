from model.game_state import GameState, GameStateType


class ManageRates(GameState):
    def start(self) -> GameStateType | None:
        customers = self._data.get_sorted_customers()

        if len(customers) == 0:
            self._view.show_no_customers_message()
            return GameStateType.SELECT_ACTION

        # Will return -1 to indicate continue.
        customer_index = self._view.show_customer_rate_select_menu(customers)

        if customer_index == -1:
            return GameStateType.SELECT_ACTION

        self._data.select_customer(customers[customer_index])
        return GameStateType.SET_RATE
