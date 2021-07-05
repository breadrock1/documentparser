from typing import Dict, Any

from Main.Extractor.WebPages.WebPageExtractor import WebPageExtractor


def __test_webpage(url: str) -> Dict[str, Any]:
    webpageParser = WebPageExtractor(url_address=url)
    content_data = webpageParser.extract_text_from_webpage()

    return content_data


def test_pdf_parser():
    test_url_1 = "https://career.habr.com/muravevstas"
    test_url_2 = "https://spb.hh.ru/resume/6b0697beff057e1f1d0039ed1f3343476d4c4c"

    assert __test_webpage(url=test_url_1) is not None \
           and __test_webpage(url=test_url_2) is not None
