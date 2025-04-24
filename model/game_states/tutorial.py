from model.game_state import GameState, GameStateType


class Tutorial(GameState):
    def start(self) -> GameStateType | None:
        self._view.show_tutorial_message()
        return GameStateType.TITLE

