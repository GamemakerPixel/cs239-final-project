from model.game_data import GameData
from model.game_state import GameState, GameStateType


class BuyData(GameState):
    def start(self) -> GameStateType | None:
        customers = self._data.get_sorted_untracked_customers()

        if len(customers) == 0:
            self._view.show_no_untracked_customers_message()
            return GameStateType.SELECT_ACTION

        # Will return -1 to indicate continue.
        customer_index = self._view.show_buy_data_select_menu(customers)

        if customer_index == -1:
            return GameStateType.SELECT_ACTION

        if self._data.get_balance() < GameData.DATA_PRICE:
            self._view.show_not_enough_money_for_purchase_message()
            return GameStateType.SELECT_ACTION

        customer = customers[customer_index]

        self._data.add_to_balance(-GameData.DATA_PRICE)
        self._data.track_customer(customer)
        
        self._view.show_new_data_on_customer(customer)

        return GameStateType.BUY_DATA
