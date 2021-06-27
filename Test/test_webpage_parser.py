from Parsers.WebPages.WebPageParser import WebPageParser


def test_pdf_parser():
    webpageParser = WebPageParser()

    test_url_1 = "https://career.habr.com/muravevstas"
    test_url_2 = "https://spb.hh.ru/resume/6b0697beff057e1f1d0039ed1f3343476d4c4c"

    text_data_1 = webpageParser.extract_text_from_webpage(url_address=test_url_1)
    text_data_2 = webpageParser.extract_text_from_webpage(url_address=test_url_2)

    assert text_data_1 is not None and text_data_2 is not None
