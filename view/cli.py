from collections.abc import Sequence

from model.game_data import Customer, GameData
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

    def show_set_rate_menu(self, customer: Customer) -> int:
        header = (
            f"What would you like to set {customer.get_name()}'s daily rate to?\n"
            f"(Their current rate is {self._format_money(customer.get_daily_rate())}.)"
            "(You can set it anywhere between "
            f"{self._format_money(Customer.MIN_RATE)}-"
            f"{self._format_money(Customer.MAX_RATE)}.)"
        )

        return cli_menus.show_bounded_int_menu(
            header,
            Customer.MIN_RATE,
            Customer.MAX_RATE
        )

    def show_no_customers_message(self) -> None:
        print("You have no customers!\n")

    def show_updated_customer_rate(self, customer: Customer) -> None:
        print(
            f"{customer.get_name()}'s rate has been set to "
            f"{self._format_money(customer.get_daily_rate())}.\n"
        )

    def show_no_untracked_customers_message(self) -> None:
        print("You are currently tracking all of your customers!\n")

    def show_buy_data_select_menu(self, customers: Sequence[Customer]) -> int:
        header = (
            "Who's driving data would you like to buy "
            f"({self._format_money(GameData.DATA_PRICE)} per customer)?\n"
        )

        customer_entries = [customer.get_name() for customer in customers]

        # -1 will indicate "Go Back" was chosen.
        return cli_menus.show_option_menu(["Go Back"] + customer_entries, header) - 1

    def show_not_enough_money_for_purchase_message(self) -> None:
        print("You don't have enough money to purchase data!\n")

    def show_new_data_on_customer(self, customer: Customer) -> None:
        print(f"You buy driving data for {customer.get_name()}.")

        bucket = customer.get_proficiency_bucket()
        print(
            f"Car manufacturers estimate their driving skill to be between "
            f"{self._format_percent(bucket.min)}-{self._format_percent(bucket.max)}."
        )
        print("As such, they have the following probabilities of crashing:")
        print(
            f"Small Crash: {self._format_percent(bucket.min_small_crash_rate)}-"
            f"{self._format_percent(bucket.max_small_crash_rate)}"
        )
        print(
            f"Large Crash: {self._format_percent(bucket.min_large_crash_rate)}-"
            f"{self._format_percent(bucket.max_large_crash_rate)}"
        )
        print("")

    def _format_money(self, amount: int) -> str:
        negative_flag = amount < 0
        
        absolute_amount = abs(amount)
        amount_str = f"${absolute_amount:,}"

        if negative_flag:
            amount_str = "-" + amount_str

        return amount_str

    def _format_percent(self, value: float) -> str:
        return f"{value:.0%}"
