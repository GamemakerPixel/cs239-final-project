import random

from model.name_manager import NameManager

_INITIAL_BALANCE = 100000
_INITIAL_CUSTOMERS = 3
_CUSTOMER_INITIAL_DAILY_RATE = 100

_NAME_MANAGER = NameManager()
_NAME_MANAGER.load_name_data()


class Customer:
    MIN_RATE = 50
    MAX_RATE = 750

    def __init__(self):
        self._name = _NAME_MANAGER.generate_name()
        self._driving_proficiency = random.random()
        self._daily_rate = _CUSTOMER_INITIAL_DAILY_RATE

    def get_name(self) -> str:
        return self._name

    def get_daily_rate(self) -> int:
        return self._daily_rate

    def set_daily_rate(self, new_rate: int) -> None:
        self._daily_rate = max(self.MIN_RATE, min(new_rate, self.MAX_RATE))


class GameData:
    def __init__(self):
        self._untracked_customers = [Customer() for _ in range(_INITIAL_CUSTOMERS)]
        self._tracked_customers: list[Customer] = []
        self._balance = _INITIAL_BALANCE
        self._selected_customer: Customer | None = None

    def get_balance(self) -> int:
        return self._balance

    def get_customer_count(self) -> int:
        return len(self._untracked_customers) + len(self._tracked_customers)

    # Sorted by first name, last name.
    def get_sorted_customers(self) -> list[Customer]:
        customers = []
        customers.extend(self._untracked_customers)
        customers.extend(self._tracked_customers)

        customers.sort(key=lambda customer: customer.get_name())

        return customers

    def get_selected_customer(self) -> Customer | None:
        return self._selected_customer

    # Ideally this would be done with a context manager, but I don't have time to
    # implement substates.
    def select_customer(self, customer: Customer) -> None:
        self._selected_customer = customer

    def deselect_customer(self) -> None:
        self._selected_customer = None
