from abc import ABC, abstractmethod
from collections.abc import Sequence

from model.game_data import Customer
from model.menu_options import ActionMenuOption, TitleMenuOption


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
