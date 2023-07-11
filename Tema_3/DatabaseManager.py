import logging
import sqlite3


class DatabaseManager:
    def __init__(self, config):
        self.config = config
        self.__conn = None

    def check_db_connection(self):
        if self.__conn is None:
            return False
        return True

    def init_db_connection(self):
        if self.check_db_connection():
            return
        try:
            conn = sqlite3.connect(self.config.db_path, check_same_thread=False)
            self.__conn = conn
            logging.info(f'[init_db_connection] - Successfully connected to {self.config.db_path} database.')
        except Exception as e:
            logging.error(f'[init_db_connection] - Failed to init db connection. {e}')
            raise Exception('Failed to init db connection.')

    def insert_data_into_db(self, sensor_name, value, timestamp):
        self.init_db_connection()
        query = f'INSERT INTO sensors_data (sensor_name, value, timestamp) VALUES ' \
                f'(\'{sensor_name}\', {value}, \'{timestamp}\')'
        try:
            self.__conn.execute(query)
            self.__conn.commit()
            logging.info(f'[insert_song_into_db] - Insertion {query} successfully executed.')
        except Exception as e:
            logging.error(f'[insert_song_into_db] - Failed executing command {query}. {e} ')

    def show_all(self):
        self.init_db_connection()
        query = f'SELECT * FROM sensors_data'
        try:
            cursor = self.__conn.execute(query)
            results = []
            for row in cursor:
                results.append([row[0], row[1], row[2], row[3]])
            logging.info(f'[show_all] - Command {query} successfully executed. Results: {results}')
            return results
        except Exception as e:
            logging.error(f'[show_all] - Failed executing command {query}. {e}')
