from Config import Config
from DatabaseManager import DatabaseManager
from ExternalAPI import run
from InputManager import InputManager
from State import State

if __name__ == '__main__':
    config = Config()
    db_manager = DatabaseManager(config)
    current_state = State()
    input_manager = InputManager(config, db_manager, current_state)
    run(input_manager, db_manager)
