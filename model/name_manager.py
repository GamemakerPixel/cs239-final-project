from pathlib import Path
import random


_DATA_ROOT = Path(__file__).parent / "data"
_FIRST_NAMES_PATH = _DATA_ROOT / "first_names.txt"
_LAST_NAMES_PATH = _DATA_ROOT / "last_names.txt"
_MAX_GENERATION_ATTEMPTS = 10
_DEFAULT_NAME = "Aidan Bensch"


class NameManager:
    def __init__(self):
        self._used_names: dict[str, set[str]] = {}
        self._first_names: list[str] = []
        self._last_names: list[str] = []

    def load_name_data(self) -> None:
        with open(_FIRST_NAMES_PATH, "r") as file:
            self._first_names = file.readlines()
        with open(_LAST_NAMES_PATH, "r") as file:
            self._last_names = file.readlines()

    # Picks a random combination of a first and last name that hasn't been used yet.
    def generate_name(self) -> str:
        attempts_left = _MAX_GENERATION_ATTEMPTS

        while attempts_left > 0:
            try:
                first_name = random.choice(self._first_names)
                last_name = random.choice(self._last_names)

                if not self._is_name_used(first_name, last_name):
                    self._use_name(first_name, last_name)
                    return first_name + " " + last_name
            except IndexError:
                return _DEFAULT_NAME

            attempts_left -= 1

        return _DEFAULT_NAME

    def _use_name(self, first_name: str, last_name: str) -> None:
        if not first_name in self._used_names:
            self._used_names[first_name] = set()

        self._used_names[first_name].add(last_name)

    def _is_name_used(self, first_name: str, last_name: str) -> bool:
        if not first_name in self._used_names:
            return False

        if not last_name in self._used_names[first_name]:
            return False

        return True


