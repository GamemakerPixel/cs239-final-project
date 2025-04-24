from collections.abc import MutableSequence, Sequence

from model.game_data import Customer
from model.game_state import GameState, GameStateType


class DailyResults(GameState):
    def start(self) -> GameStateType | None:
        customers = self._data.get_sorted_customers()

        self._handle_leaving_customers(customers)

        self._handle_daily_fees(customers)

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
    
    def _handle_daily_fees(self, customers: Sequence[Customer]) -> None:
        total = 0

        for customer in customers:
            total += customer.get_daily_rate()

        self._data.add_to_balance(total)

        self._view.show_daily_fees_collected_message(total)

#You collected a total of $850 from your customers in daily fees.

#The following customers made insurance claims:
#- Bert Scute: Large Crash (-$8500)
#- Bob Smith: Small Crash (-$650)

#In total, these claims cost you $9150.

#You gained a new customer: Sandra Claire (+$2000 upfront)

#Net profit for the day: -$6300
