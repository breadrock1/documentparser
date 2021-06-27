from time import time_ns
from typing import Dict, Optional
from requests import get, Response
from bs4 import BeautifulSoup
from logging import exception


class WebPageParser(object):
    def __init__(self, url_address: str):
        self.url_address = url_address

    def __write_dom_object_to_file(self, content: Optional[bytes]) -> str:

        def __generate_file_name() -> str:
            return f'{time_ns()}_webpage.html'

        file_name = __generate_file_name()

        with open(f'/tmp/{file_name}', 'w+') as file:
            file.write(content.decode('utf-8'))
            file.close()

        return file_name

    # TODO: How include ssl-cert??
    def __send_get_request(self) -> Response or None:
        try:
            response = get(
                url=self.url_address,
                allow_redirects=True,
                verify=False
            )
        except Exception as e:
            exception(msg=f'[!]\tFailed to send request: {e}')
            return None

        if response.status_code != 200:
            return None

        return response.content

    def extract_text_from_webpage(self) -> Dict[str, str or Dict]:
        response = self.__send_get_request()
        html_file_path = self.__write_dom_object_to_file(content=response)

        soup = BeautifulSoup(html_file_path)
        test = ''.join([repr(string) for string in soup.stripped_strings])

        return {'webpage': test}
