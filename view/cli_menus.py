from collections.abc import Sequence
from pathlib import Path

_OPTION_FORMAT = "(%d) %s"


def show_option_menu(options: Sequence[str], header: str = "") -> int:
    while True:
        if header:
            print(header + "\n");

        for index, option in enumerate(options):
            print(_OPTION_FORMAT % (index, option))
        print("")

        user_input = input()
        print("")

        try:
            index_selected = int(user_input)

            if index_selected >= 0 and index_selected < len(options):
                return index_selected
        except ValueError:
            continue


def show_message_from_file(text_file_path: Path) -> None:
    with open(text_file_path, "r") as file:
        print(file.read())

