from pathlib import Path
from typing import Any, Dict
from logging import info, warning

from Parsers.Documents.DocParser import DocParser
from Parsers.Documents.PdfParser import PdfParser
from Parsers.WebPages.WebPageParser import WebPageParser


class ParserManager(object):
    @staticmethod
    def parseWebpage(link_to_webpage: str) -> Dict[str, Any]:
        info(msg='[+]\tStarting parsing webpage process...')

        text_data = WebPageParser.extract_text_from_webpage(url_address=link_to_webpage)

        info(msg='[+]\tThe scraping process has been done!')

        return text_data

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
