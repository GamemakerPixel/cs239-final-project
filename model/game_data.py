from collections.abc import Sequence
import random

from model.name_manager import NameManager

_INITIAL_BALANCE = 100000
_INITIAL_CUSTOMERS = 3
_CUSTOMER_INITIAL_DAILY_RATE = 100

_NAME_MANAGER = NameManager()
_NAME_MANAGER.load_name_data()


class ProficiencyBucket:
    BUCKET_SIZE = 0.2

    def __init__(
            self,
            min: float,
            max: float,
            min_small_crash_rate: float,
            max_small_crash_rate: float,
            min_large_crash_rate: float,
            max_large_crash_rate: float
    ):
        self.min = min
        self.max = max
        self.min_small_crash_rate = min_small_crash_rate
        self.max_small_crash_rate = max_small_crash_rate
        self.min_large_crash_rate = min_large_crash_rate
        self.max_large_crash_rate = max_large_crash_rate


class Customer:
    MIN_RATE = 50
    MAX_RATE = 750

    _MIN_FAIR_RATE = 100
    _MAX_FAIR_RATE = 700

    _MIN_SMALL_CRASH_RATE = 0.04
    _MAX_SMALL_CRASH_RATE = 0.2
    _MIN_LARGE_CRASH_RATE = 0.0
    _MAX_LARGE_CRASH_RATE = 0.2

    _CHANCE_OF_LEAVING_AT_FAIR_PRICE = 0.1

    def __init__(self):
        self._name = _NAME_MANAGER.generate_name()
        self._driving_proficiency = random.random()
        self._daily_rate = _CUSTOMER_INITIAL_DAILY_RATE

    def get_name(self) -> str:
        return self._name

    def get_daily_rate(self) -> int:
        return self._daily_rate

    def get_proficiency_bucket(self) -> ProficiencyBucket:
        upper_bounds = [
            x * ProficiencyBucket.BUCKET_SIZE
            for x in range(1, int(1.0/ProficiencyBucket.BUCKET_SIZE) + 1)
        ]

        for upper_bound in upper_bounds:
            if self._driving_proficiency < upper_bound:
                lower_bound = upper_bound - ProficiencyBucket.BUCKET_SIZE
                return ProficiencyBucket(
                    lower_bound,
                    upper_bound,
                    self._get_small_crash_rate(upper_bound),
                    self._get_small_crash_rate(lower_bound),
                    self._get_large_crash_rate(upper_bound),
                    self._get_large_crash_rate(lower_bound)
                )

    def set_daily_rate(self, new_rate: int) -> None:
        self._daily_rate = max(self.MIN_RATE, min(new_rate, self.MAX_RATE))

    def leaves_at_current_rate(self) -> bool:
        chance = self._get_chance_of_leaving()
        return random.random() < chance

    def _get_chance_of_leaving(self) -> float:
        return (
            self._CHANCE_OF_LEAVING_AT_FAIR_PRICE * (self._daily_rate - self.MIN_RATE) ** 2
            / (self._get_fair_rate() - self._daily_rate) ** 2
        )

    # Yes these would be better as class methods, but I'm not sure the constants would
    # be accessable though cls. (I don't really have time to find out.)
    def _get_small_crash_rate(self, proficiency: float) -> float:
        return self._lerp(
            self._MAX_SMALL_CRASH_RATE,
            self._MIN_SMALL_CRASH_RATE,
            proficiency
        )

    def _get_large_crash_rate(self, proficiency: float) -> float:
        return self._lerp(
            self._MAX_LARGE_CRASH_RATE,
            self._MIN_LARGE_CRASH_RATE,
            proficiency
        )

    def _get_fair_rate(self) -> int:
        return self._lerp(
            self._MAX_FAIR_RATE,
            self._MIN_FAIR_RATE,
            self._driving_proficiency
        )
    
    def _lerp(self, start: float, end: float, time: float) -> float:
        return (start * (1.0 - time)) + (end * time)



class GameData:
    DATA_PRICE = 500

    def __init__(self):
        # These should probably be sets.
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

        self.sort_customer_list(customers)

        return customers

    def get_sorted_untracked_customers(self) -> list[Customer]:
        customers = self._untracked_customers[:]

        self.sort_customer_list(customers)

        return customers

    def get_sorted_tracked_customers(self) -> list[Customer]:
        customers = self._tracked_customers[:]

        self.sort_customer_list(customers)

        return customers

    def sort_customer_list(self, customers: Sequence[Customer]) -> None:
        customers.sort(key=lambda customer: customer.get_name())

    def get_selected_customer(self) -> Customer | None:
        return self._selected_customer

    def add_to_balance(self, amount: int) -> None:
        self._balance += amount

    # Ideally this would be done with a context manager, but I don't have time to
    # implement substates.
    def select_customer(self, customer: Customer) -> None:
        self._selected_customer = customer

    def deselect_customer(self) -> None:
        self._selected_customer = None

    def track_customer(self, customer: Customer) -> None:
        if not customer in self._untracked_customers:
            return

        self._untracked_customers.remove(customer)
        self._tracked_customers.append(customer)

    def remove_customer(self, customer: Customer) -> None:
        if customer in self._untracked_customers:
            self._untracked_customers.remove(customer)
        elif customer in self._tracked_customers:
            self._tracked_customers.remove(customer)
