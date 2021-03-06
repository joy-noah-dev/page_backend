# Python packages
import os
from os import path

# External packages
from dotenv import load_dotenv
from flask import Flask, jsonify, got_request_exception
from flask_cors import CORS
from api import set_up_api

load_dotenv(path.join(path.dirname(__file__), '.env'))

app = Flask(__name__)
CORS(app)
app.config.from_object('config')

@app.errorhandler(Exception)
def exception_error(e):
    """
    Return default 500 code when an unhandled exception is raised.
    :param e: Exception instance.
    :return: Response instance.
    """
    return jsonify({'message': e.description}), e.code

set_up_api(app)