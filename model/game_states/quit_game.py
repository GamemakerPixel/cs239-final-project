from model.game_state import GameState, GameStateType


class Quit(GameState):
    def start(self) -> GameStateType | None:
        self._view.show_quit_message()

        # Returning None to end the game.
        return None

