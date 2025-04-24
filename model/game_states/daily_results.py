from collections.abc import MutableSequence, Sequence

from model.game_data import CrashType, Customer, GameData
from model.game_state import GameState, GameStateType


class DailyResults(GameState):
    def start(self) -> GameStateType | None:
        customers = self._data.get_sorted_customers()

        self._handle_leaving_customers(customers)

        net_profit = 0
        net_profit += self._handle_daily_fees(customers)
        net_profit -= self._handle_insurance_claims(customers)
        net_profit += self._handle_new_customer()

        self._view.show_net_profit(net_profit)

        if self._data.is_game_won():
            return GameStateType.GAME_WON
        elif self._data.is_bankrupt():
            return GameStateType.BANKRUPT

        return GameStateType.SELECT_ACTION

    def _handle_leaving_customers(self, customers: MutableSequence[Customer]) -> None:
        leaving_customers: list[Customer] = []

        for customer in customers:
            if customer.leaves_at_current_rate():
                customers.remove(customer)
                self._data.remove_customer(customer)
                leaving_customers.append(customer)

        if len(leaving_customers) == 0:
            self._view.show_no_customers_leaving_message()
            return

        self._view.show_leaving_customers_message(leaving_customers)
    
    def _handle_daily_fees(self, customers: Sequence[Customer]) -> int:
        total = 0

        for customer in customers:
            total += customer.get_daily_rate()

        self._data.add_to_balance(total)

        self._view.show_daily_fees_collected_message(total)

        return total
    
    def _handle_insurance_claims(self, customers: Sequence[Customer]) -> int:
        claims: dict[Customer, tuple[CrashType, int]] = {}
        total = 0

        for customer in customers:
            crash_type = customer.gets_in_crash()

            if crash_type == CrashType.NONE:
                continue

            cost = GameData.get_crash_cost(crash_type)
            claims[customer] = (crash_type, cost)
            total += cost

        self._data.add_to_balance(-total)

        if len(claims) == 0:
            self._view.show_no_claims_message()
            return 0
        
        self._view.show_claims(claims)

        return total

    def _handle_new_customer(self) -> int:
        customer = Customer()
        self._data.add_customer(customer)
        self._data.add_to_balance(GameData.NEW_CUSTOMER_UPFRONT)

        self._view.show_new_customer(customer, GameData.NEW_CUSTOMER_UPFRONT)

        return GameData.NEW_CUSTOMER_UPFRONT


