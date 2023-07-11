import json
import os
import time


class InputManager:
    def __init__(self, config, db_manager, current_state):
        self.config = config
        self.db_manager = db_manager
        self.current_state = current_state
        self.already_parsed = []

    def update_current_state(self, sensor):
        if sensor['sensor_name'] == 'motion_inside':
            self.current_state.motion_inside = sensor['value']
        elif sensor['sensor_name'] == 'motion_outside':
            self.current_state.motion_outside = sensor['value']
        else:
            self.current_state.force = sensor['value']

    def parse_input(self):
        for file in os.listdir(self.config.input_path):
            time.sleep(1)
            path = os.path.join(self.config.input_path, file)
            if path in self.already_parsed:
                continue
            self.already_parsed.append(path)
            with open(path, 'r') as f:
                sensors_data = json.load(f)
                sensors_data = sensors_data['sensors']
                for sensor in sensors_data:
                    self.update_current_state(sensor)
                    self.db_manager.insert_data_into_db(sensor['sensor_name'], sensor['value'], sensor['timestamp'])
