from pathlib import Path
from Main.Documents.PdfParser import PdfParser


def test_pdf_parser():
    path_to_file = (Path() / 'TestFiles' / 'test_pdf_file.pdf').absolute()
    pdfParser = PdfParser(file_path=path_to_file)

    assert pdfParser.extract_text_from_file()
