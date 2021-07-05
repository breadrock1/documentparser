from pathlib import Path
from Main.Extractor.Documents import PdfExtractor


def test_pdf_parser():
    path_to_file = (Path() / 'TestFiles' / 'test_pdf_file.pdf').absolute()
    pdfParser = PdfExtractor(file_path=path_to_file)

    assert pdfParser.extract_text_from_file()
