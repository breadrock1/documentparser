from pathlib import Path
from typing import Any, Dict
from logging import info, warning

from Parsers.Documents.DocParser import DocParser
from Parsers.Documents.PdfParser import PdfParser
from Parsers.WebPages.WebPageParser import WebPageParser


class ParserManager(object):
    @staticmethod
    def parseExtractedTextData(extracted_data: str) -> Dict[str, Any]:
        # TODO: realize this method
        return {'data': extracted_data}

    @staticmethod
    def parseWebpage(link_to_webpage: str) -> Dict[str, Any]:
        info(msg='[+]\tStarting parsing webpage process...')

        webPageParser = WebPageParser(url_address=link_to_webpage)
        text_data = webPageParser.extract_text_from_webpage()

        info(msg='[+]\tThe scraping process has been done!')

        return ParserManager.parseExtractedTextData(extracted_data=text_data)

    @staticmethod
    def parseDocument(path_to_file: str) -> Dict[str, Any]:
        info(msg='[+]\tStarting parsing document process...')

        extension = Path(path_to_file).suffix

        if extension == ".pdf":
            pdfParser = PdfParser(file_path=path_to_file)
            text_data = pdfParser.extract_text_from_file()

        elif extension == ".doc" or extension == ".docx":
            docParser = DocParser(file_path=path_to_file)
            text_data = docParser.extract_text_from_file()

        else:
            warning(msg='Unknown file extension. Please check the extension is correct!')
            return {}

        info(msg='[+]\tThe scraping process has been done!')

        return ParserManager.parseExtractedTextData(extracted_data=text_data)
