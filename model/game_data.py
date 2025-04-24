import random

from model.name_manager import NameManager

_INITIAL_BALANCE = 100000
_INITIAL_CUSTOMERS = 3
_CUSTOMER_INITIAL_DAILY_RATE = 100

_NAME_MANAGER = NameManager()
_NAME_MANAGER.load_name_data()


class Customer:
    def __init__(self):
        self._name = _NAME_MANAGER.generate_name()
        self._driving_proficiency = random.random()
        self._daily_rate = _CUSTOMER_INITIAL_DAILY_RATE


class GameData:
    def __init__(self):
        self._untracked_customers = [Customer() for _ in range(_INITIAL_CUSTOMERS)]
        self._tracked_customers: list[Customer] = []
        self._balance = _INITIAL_BALANCE

    def get_balance(self) -> int:
        return self._balance

    def get_customer_count(self) -> int:
        return len(self._untracked_customers) + len(self._tracked_customers)
