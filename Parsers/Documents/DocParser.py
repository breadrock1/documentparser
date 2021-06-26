import docx2txt

from typing import Dict
from logging import exception


class DocParser(object):
    @staticmethod
    def extract_text_from_file(file_path: str) -> Dict[str, str or Dict]:
        try:
            return {'doc_file': docx2txt.process(file_path)}

        except Exception as e:
            exception(msg=f'Failed while parsing Doc-file: {e}')
            return {'doc_file': ''}
