from typing import Dict
from requests import get
from bs4 import BeautifulSoup
from logging import exception, info


class WebPageParser(object):
    @staticmethod
    def __send_get_request(url: str):
        try:
            response = get(
                url=url,
                cert=('/Path/To/File.key', '/Path/to/File.perm'),
                allow_redirects=True
            )
        except Exception as e:
            exception(msg=f'[!]\tFailed to send request: {e}')
            return None

        if response.status_code != 200:
            return None

    @staticmethod
    def extract_text_from_webpage(url_address: str) -> Dict[str, str or Dict]:
        html = WebPageParser.__send_get_request(url=url_address)

        soup = BeautifulSoup(html)
        test = ''.join([repr(string) for string in soup.stripped_strings])

        return {}
