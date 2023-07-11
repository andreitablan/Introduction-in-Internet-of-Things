import logging

from flask import Flask, jsonify

app = Flask(__name__)

input_manager = None
db_manager = None


@app.route('/sensors_data', methods=['GET'])
def get_data():
    global input_manager
    global db_manager
    input_manager.parse_input()
    data = {
        "raise_alert": input_manager.current_state.is_security_alert(),
        "sensors_data": db_manager.show_all()
    }
    logging.info(f'[get_data] - {data}')
    response = jsonify(data)
    response.headers.add('Access-Control-Allow-Origin', 'http://127.0.0.1:5501')
    return response


def run(inp, db):
    global input_manager
    global db_manager
    input_manager = inp
    db_manager = db

    app.run(port=5001)
