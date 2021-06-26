from typing import Dict
from requests import get
from bs4 import BeautifulSoup
from logging import exception, info


class WebPageParser(object):
    def __init__(self):
        self.parsed_data = {}

    def __parse_html_data(self, html: bytes) -> str:
        soup = BeautifulSoup(html)
        return ''.join([repr(string) for string in soup.stripped_strings])

    # TODO: Need test this method to get request with ssl-cert
    def __get_html_data(self, link: str) -> bytes or None:
        try:
            response = get(
                url=link,
                cert=('/Path/To/File.key', '/Path/to/File.perm'),
                allow_redirects=True
            )
        except Exception as e:
            exception(msg=f'[!]\tFailed to send request: {e}')
            return None

        if response.status_code != 200:
            return None

        return response.content

    def get_parsed_data(self) -> Dict[str, str or Dict]:
        return self.parsed_data

    def scrape(self, link: str) -> None:

        info(msg='[*]\tStart parsing web pages process...', level=0)

        html = self.__get_html_data(link=link)

        if not html:
            return

        self.parsed_data.update(
            self.__parse_html_data(html=html)
        )

        info(msg='[+] The parsing web page has been done!', level=0)
