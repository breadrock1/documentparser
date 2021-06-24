from pathlib import Path
from typing import Any, Dict
from logging import info, warning

from Parsers.DocParser import DocParser
from Parsers.PdfParser import PdfParser


class ParserManager(object):
    def __init__(self):
        pass

    @staticmethod
    def parseDocument(path_to_file: str) -> Dict[str, Any]:
        info(msg='[+]\tStarting parsing document process...')

        extension = Path(path_to_file).suffix

        if extension == ".pdf":
            text_data = PdfParser.extract_text_from_file(path_to_file)
        elif extension == ".doc" or extension == ".docx":
            text_data = DocParser.extract_text_from_file(path_to_file)
        else:
            warning(msg='Unknown file extension. Please check the extension is correct!')
            return {}

        info(msg='[+]\tThe scraping process has been done!')

        return text_data

    @staticmethod
    def parseWebPage(link: str) -> Dict[str, Any]:
        info(msg='[+]\tStarting parsing document process...')

        info(msg='[+]\tThe scraping process has been done!')

        return {}
