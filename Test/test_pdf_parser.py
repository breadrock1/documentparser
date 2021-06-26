from pathlib import Path
from Parsers.Documents.PdfParser import PdfParser


def test_pdf_parser():
    pdfParser = PdfParser()
    path_to_file = (Path() / 'TestFiles' / 'test_pdf_file.pdf').absolute()

    assert pdfParser.extract_text_from_file(path_to_file)
