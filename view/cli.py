from collections.abc import Sequence

from model.game_data import Customer
from model.menu_options import ActionMenuOption, TitleMenuOption
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

    def show_company_status(self, balance: int, customers: int) -> None:
        print(
            f"You currently have {self._format_money(balance)} and {customers} "
            "customers."
        )

    def show_action_menu(self) -> ActionMenuOption:
        options = [
            ActionMenuOption.CONTINUE,
            ActionMenuOption.RATES,
            ActionMenuOption.VIEW_DATA,
            ActionMenuOption.BUY_DATA,
            ActionMenuOption.QUIT,
        ]
        text_options = [
            "Continue",
            "View/Set Customer Daily Insurance Rates",
            "View Known Customer Driving Data",
            "Buy Customer Driving Data",
            "Quit Game",
        ]

        return options[cli_menus.show_option_menu(
            text_options,
            "What would you like to do?"
        )]

    def show_customer_rate_select_menu(self, customers: Sequence[Customer]) -> int:
        header = (
            "Here are your customers and their current rates.\n"
            "Select a customer to change their rate."
        )

        customer_entries = [
            f"{customer.get_name()}: {self._format_money(customer.get_daily_rate())}"
            for customer in customers
        ]

        # -1 will indicate "Go Back" was chosen.
        return cli_menus.show_option_menu(["Go Back"] + customer_entries, header) - 1

    def _format_money(self, amount: int) -> str:
        negative_flag = amount < 0
        
        absolute_amount = abs(amount)
        amount_str = f"${absolute_amount:,}"

        if negative_flag:
            amount_str = "-" + amount_str

        return amount_str
