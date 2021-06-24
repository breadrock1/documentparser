from logging import exception
from flask import Flask, request, abort

from Parsers.ParserManager import ParserManager


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def indexPage():
    return {}


@app.route('/webpage_parsing', methods=['POST'])
def launchWebPageParsing():

    def _getWebPageLink() -> str:
        try:
            return json_data.get('link')
        except KeyError as e:
            exception(msg=f'Failed to get link field from request... {e}')
            abort(400)

    if request.method == 'POST':
        json_data = request.get_json()
        return ParserManager.parseWebPage(link=_getWebPageLink())

    abort(405)


@app.route('/documents_parsing', methods=['POST'])
def launchDocumentParsing():

    def _getDocumentFile() -> str:
        try:
            return json_data.get('link')
        except KeyError as e:
            exception(msg=f'Failed to get document file path from request... {e}')
            abort(400)

    if request.method == 'POST':
        json_data = request.get_json()
        return ParserManager.parseDocument(path_to_file=_getDocumentFile())

    abort(405)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
