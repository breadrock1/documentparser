import json

from time import sleep
from pathlib import Path
from requests import post
from flask_backend_run import app
from multiprocessing import Process


result_full_scraping_response = {
    'link': 'fdg'
}


def _runBackendApp() -> None:
    app.run(host='127.0.0.1', port=7654)


def _createProcess() -> Process:
    return Process(target=_runBackendApp, name='flask_backend_process')


def _sendRequestToParsing(mode: str, json_data: json) -> json:
    response = post(
        url=f'http://127.0.0.1:7654/{mode}',
        json=json_data
    )

    return response.json()


def test_backend_module():
    backend_process = _createProcess()
    backend_process.start()

    sleep(2)

    resume_url = 'https://spb.hh.ru/resume/6b0697beff057e1f1d0039ed1f3343476d4c4c'
    path_to_file = (Path() / 'TestFiles' / 'test_pdf_file.pdf').absolute()

    try:
        response_webpage_parsing = _sendRequestToParsing(
            mode='webpage_parsing',
            json_data={'link': resume_url}
        )
        response_document_parsing = _sendRequestToParsing(
            mode='documents_parsing',
            json_data={'file_path': path_to_file}
        )

        assert response_webpage_parsing == {}
        assert response_document_parsing == {}

    except Exception as e:
        print(f'Error while executing request. {e.with_traceback()}')

    finally:
        backend_process.kill()
