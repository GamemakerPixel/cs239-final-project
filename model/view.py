from abc import ABC, abstractmethod

from model.menu_options import TitleMenuOption


class View(ABC):
    @abstractmethod
    def show_title(self) -> None:
        pass

    @abstractmethod
    def show_title_menu(self) -> TitleMenuOption:
        pass
