import docx2txt

from typing import Dict
from logging import exception


class DocParser(object):
    def __init__(self, file_path: str):
        self.file_path = file_path

    def __extract_data(self) -> str:
        try:
            return docx2txt.process(self.file_path)

        except Exception as e:
            exception(msg=f'Failed while parsing Doc-file: {e}')
            return ''

    def extract_text_from_file(self) -> Dict[str, str or Dict]:
        return {'doc_file': self.__extract_data()}
