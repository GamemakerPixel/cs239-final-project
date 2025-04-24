from model.game_state import GameState, GameStateType


class ViewData(GameState):
    def start(self) -> GameStateType | None:
        customers = self._data.get_sorted_tracked_customers()

        if len(customers) == 0:
            self._view.show_no_tracked_customers_message()
            return GameStateType.SELECT_ACTION

        self._view.show_tracked_customer_data(customers)
        return GameStateType.SELECT_ACTION
