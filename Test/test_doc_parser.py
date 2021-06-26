from pathlib import Path
from Parsers.Documents.DocParser import DocParser


def test_doc_parser():
    docParser = DocParser()
    path_to_file = (Path() / 'Test' / 'TestFiles' / 'test_doc_file.doc').absolute()

    assert docParser.extract_text_from_file(path_to_file)
