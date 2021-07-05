from pathlib import Path
from typing import Any, Dict
from logging import info, warning

from Main.Parser.Parser import Parser
from Main.Extractor.Documents.DocExtractor import DocExtractor
from Main.Extractor.Documents.PdfExtractor import PdfExtractor
from Main.Extractor.WebPages.WebPageExtractor import WebPageExtractor


class ParserManager(object):
    @staticmethod
    def parseExtractedTextData(extracted_data: str) -> Dict[str, Any]:
        parser = Parser()

        return parser.parse(text_data=extracted_data)

    @staticmethod
    def parseWebpage(link_to_webpage: str) -> Dict[str, Any]:
        info(msg='[+]\tStarting parsing webpage process...')

        webPageExtractor = WebPageExtractor(url_address=link_to_webpage)
        text_data = webPageExtractor.extract_text_from_webpage()

        info(msg='[+]\tThe scraping process has been done!')

        return ParserManager.parseExtractedTextData(extracted_data=text_data)

    @staticmethod
    def parseDocument(path_to_file: str) -> Dict[str, Any]:
        info(msg='[+]\tStarting parsing document process...')

        extension = Path(path_to_file).suffix

        if extension == ".pdf":
            pdfExtractor = PdfExtractor(file_path=path_to_file)
            text_data = pdfExtractor.extract_text_from_file()

        elif extension == ".doc" or extension == ".docx":
            docExtractor = DocExtractor(file_path=path_to_file)
            text_data = docExtractor.extract_text_from_file()

        else:
            warning(msg='Unknown file extension. Please check the extension is correct!')
            return {}

        info(msg='[+]\tThe scraping process has been done!')

        return ParserManager.parseExtractedTextData(extracted_data=text_data)
