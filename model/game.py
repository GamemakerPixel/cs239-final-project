from model import state_factory
from model.game_data import GameData
from model.game_state import GameStateType, GameState
from model.view import View


class Game:
    def __init__(self, view: View):
        self._view = view

    def begin(self) -> None:
        next_state = GameStateType.TITLE

        while next_state:
            # Reload the game when we go to the main menu.
            if next_state == GameStateType.TITLE:
                self._data = GameData()

            state = state_factory.construct_state(next_state, self._view, self._data)
            next_state = state.start()
