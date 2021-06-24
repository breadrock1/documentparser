from flask import Flask, request, abort


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def indexPage():
    return {}


@app.route('/webpage_parsing', methods=['POST'])
def launchWebPageParsing():
    if request.method == 'POST':
        pass

    abort(405)


@app.route('/documents_parsing', methods=['POST'])
def launchDocumentParsing():
    if request.method == 'POST':
        pass

    abort(405)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
