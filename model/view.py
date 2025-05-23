from abc import ABC, abstractmethod
from collections.abc import Mapping, Sequence

from model.game_data import CrashType, Customer
from model.menu_options import (
    ActionMenuOption,
    BankruptOption,
    GameWonOption,
    TitleMenuOption
)


class View(ABC):
    @abstractmethod
    def show_title(self) -> None:
        pass

    @abstractmethod
    def show_title_menu(self) -> TitleMenuOption:
        pass

    @abstractmethod
    def show_tutorial_message(self) -> None:
        pass

    @abstractmethod
    def show_quit_message(self) -> None:
        pass

    @abstractmethod
    def show_company_status(self, balance: int, customers: int) -> ActionMenuOption:
        pass
    
    @abstractmethod
    def show_action_menu(self) -> None:
        pass

    @abstractmethod
    def show_customer_rate_select_menu(self, customers: Sequence[Customer]) -> int:
        pass

    @abstractmethod
    def show_set_rate_menu(self, customer: Customer) -> int:
        pass

    @abstractmethod
    def show_no_customers_message(self) -> None:
        pass

    @abstractmethod
    def show_updated_customer_rate(self, customer: Customer) -> None:
        pass

    @abstractmethod
    def show_no_untracked_customers_message(self) -> None:
        pass

    @abstractmethod
    def show_buy_data_select_menu(self, customers: Sequence[Customer]) -> int:
        pass

    @abstractmethod
    def show_not_enough_money_for_purchase_message(self) -> None:
        pass

    @abstractmethod
    def show_new_data_on_customer(self, customer: Customer) -> None:
        pass

    @abstractmethod
    def show_no_tracked_customers_message(self) -> None:
        pass

    @abstractmethod
    def show_tracked_customer_data(self, customers: Sequence[Customer]) -> None:
        pass

    @abstractmethod
    def show_no_customers_leaving_message(self) -> None:
        pass

    @abstractmethod
    def show_leaving_customers_message(self, customers: Sequence[Customer]) -> None:
        pass

    @abstractmethod
    def show_daily_fees_collected_message(self, total: int) -> None:
        pass

    @abstractmethod
    def show_no_claims_message(self) -> None:
        pass

    @abstractmethod
    def show_claims(self, claims: Mapping[Customer, tuple[CrashType, int]]) -> None:
        pass

    @abstractmethod
    def show_new_customer(self, customer: Customer, upfront: int) -> None:
        pass

    @abstractmethod
    def show_net_profit(self, net_profit: int) -> None:
        pass

    @abstractmethod
    def show_game_won_menu(self) -> GameWonOption:
        pass

    @abstractmethod
    def show_bankrupt_menu(self) -> BankruptOption:
        pass
