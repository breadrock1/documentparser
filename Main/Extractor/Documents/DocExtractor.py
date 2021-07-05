import docx2txt

from logging import exception

from Main.Extractor.Documents import Extractor


class DocExtractor(Extractor):
    def __init__(self, file_path: str):
        super().__init__()

        self.file_path = file_path

    def __extract_data(self) -> str:
        try:
            return docx2txt.process(self.file_path)

        except Exception as e:
            exception(msg=f'Failed while parsing Doc-file: {e}')
            return ''

    def extract_text_from_file(self) -> str:
        return self.__extract_data()
