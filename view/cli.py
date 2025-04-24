from model.menu_options import TitleMenuOption
from model.view import View
from view import cli_menus
from view.message_data_root import MESSAGE_DATA_PATH

class CliView(View):
    def show_title(self) -> None:
        print("Welcome to Car Insurance Simulator!\n")

    def show_title_menu(self) -> TitleMenuOption:
        options = [
            TitleMenuOption.PLAY,
            TitleMenuOption.TUTORIAL,
            TitleMenuOption.QUIT,
        ]
        text_options = [
            "Play",
            "Tutorial",
            "Quit",
        ]

        return options[cli_menus.show_option_menu(text_options, "Main Menu")]

    def show_tutorial_message(self) -> None:
        cli_menus.show_message_from_file(MESSAGE_DATA_PATH / "tutorial.txt")

    def show_quit_message(self) -> None:
        cli_menus.show_message_from_file(MESSAGE_DATA_PATH / "quit.txt")

