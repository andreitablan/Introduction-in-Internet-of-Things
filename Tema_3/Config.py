import logging


class Config:
    def __init__(self):
        self.input_path = r'.\Input'
        self.db_path = r'.\Utils\Storage.db'
        self.log_file_path = r'.\Logs\security_log.txt'
        logging.basicConfig(filename=self.log_file_path, level=logging.DEBUG,
                            format="[%(asctime)s][%(levelname)s] %(message)s", filemode="w")
