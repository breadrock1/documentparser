import json
from pathlib import Path
from logging import exception
from flask import Flask, request, abort
from werkzeug.utils import secure_filename

from Main.ParserManager import ParserManager


UPLOAD_FOLDER = Path() / 'Upload'
ALLOWED_EXTENSIONS = ['txt', 'pdf', 'doc', 'docx']

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


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


@app.route('/documents_parsing', methods=['GET', 'POST'])
def launchDocumentParsing():
    if request.method == 'GET':
        return {}

    elif request.method == 'POST':
        json_data = request.get_json()
        file_path = __getValueByKeyFromJson(json_data=json_data, key='file_path')

        return ParserManager.parseDocument(path_to_file=file_path)

    abort(405)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/upload_and_analyse_file')
def uploadFile():
    if request.method == 'GET':
        return '''
            <!doctype html>
            <title>Upload new File</title>
            <h1>Upload new File</h1>
            <form action="" method=post enctype=multipart/form-data>
                <p><input type=file name=file>
                <input type=submit value=Upload>
            </form>
        '''

    if request.method == 'POST':
        file = request.files['file']

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = UPLOAD_FOLDER.joinpath(filename)
            file.save(file_path)

            return ParserManager.parseDocument(path_to_file=file_path)

    abort(405)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
