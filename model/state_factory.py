from model.game_data import GameData
from model.game_state import GameState, GameStateType
from model.game_states.bankrupt import Bankrupt
from model.game_states.buy_data import BuyData
from model.game_states.daily_results import DailyResults
from model.game_states.game_won import GameWon
from model.game_states.manage_rates import ManageRates 
from model.game_states.select_action import SelectAction
from model.game_states.set_rate import SetRate
from model.game_states.title import Title
from model.game_states.tutorial import Tutorial
from model.game_states.quit_game import Quit
from model.game_states.view_data import ViewData
from model.view import View


_STATE_CLASS_MAPPING = {
    GameStateType.TITLE: Title,
    GameStateType.SHOW_TUTORIAL: Tutorial,
    GameStateType.QUIT: Quit,
    GameStateType.SELECT_ACTION: SelectAction,
    GameStateType.MANAGE_RATES: ManageRates,
    GameStateType.SET_RATE: SetRate,
    GameStateType.VIEW_DATA: ViewData,
    GameStateType.BUY_DATA: BuyData,
    GameStateType.DAILY_RESULTS: DailyResults,
    GameStateType.GAME_WON: GameWon,
    GameStateType.BANKRUPT: Bankrupt,
}


def construct_state(
        state_type: GameStateType,
        view: View,
        data: GameData
) -> GameState:
    state_class = _STATE_CLASS_MAPPING[state_type]
    return state_class(view, data)
