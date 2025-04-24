from model.game_data import GameData
from model.game_state import GameState, GameStateType
from model.game_states.manage_rates import ManageRates 
from model.game_states.select_action import SelectAction
from model.game_states.set_rate import SetRate
from model.game_states.title import Title
from model.game_states.tutorial import Tutorial
from model.game_states.quit_game import Quit
from model.view import View


_STATE_CLASS_MAPPING = {
    GameStateType.TITLE: Title,
    GameStateType.SHOW_TUTORIAL: Tutorial,
    GameStateType.QUIT: Quit,
    GameStateType.SELECT_ACTION: SelectAction,
    GameStateType.MANAGE_RATES: ManageRates,
    GameStateType.SET_RATE: SetRate,
    GameStateType.VIEW_DATA: None,
    GameStateType.BUY_DATA: None,
    GameStateType.DAILY_RESULTS: None,
}


def construct_state(
        state_type: GameStateType,
        view: View,
        data: GameData
) -> GameState:
    state_class = _STATE_CLASS_MAPPING[state_type]
    return state_class(view, data)
