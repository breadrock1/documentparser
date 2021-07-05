from pathlib import Path
from Main.Documents.DocParser import DocParser


def test_doc_parser():
    path_to_file = (Path() / 'Test' / 'TestFiles' / 'test_doc_file.doc').absolute()
    docParser = DocParser(file_path=path_to_file)

    assert docParser.extract_text_from_file()
