import json

from typing import Dict, Union
from flask import Flask, request, abort


app = Flask(__name__)


@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def indexPage():
    if request.method == 'GET':
        return {}

    abort(405)


@app.route('/documents_parsing', methods=['POST'])
def launchFullScraping():
    if request.method == 'POST':
        pass

    abort(405)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
