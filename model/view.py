from abc import ABC, abstractmethod

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
