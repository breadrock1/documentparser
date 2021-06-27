import json
from logging import exception
from flask import Flask, request, abort

from Parsers.ParserManager import ParserManager


app = Flask(__name__)


def __getValueByKeyFromJson(json_data: json, key: str) -> str:
    try:
        return json_data.get(key)
    except KeyError as e:
        exception(msg=f'Failed to get link field from request... {e}')
        abort(400)


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def indexPage():
    return {}


@app.route('/webpage_parsing', methods=['POST'])
def launchWebPageParsing():
    if request.method == 'POST':
        json_data = request.get_json()
        link = __getValueByKeyFromJson(json_data=json_data, key='link')

        return ParserManager.parseWebPage(link=link)

    abort(405)


# TODO: Need add ability to load files by POST method request
@app.route('/documents_parsing', methods=['GET', 'POST'])
def launchDocumentParsing():
    if request.method == 'GET':
        return {}

    elif request.method == 'POST':
        json_data = request.get_json()
        file_path = __getValueByKeyFromJson(json_data=json_data, key='file_path')

        return ParserManager.parseDocument(path_to_file=file_path)

    abort(405)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
