import io

from logging import exception

from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager

from Main.Extractor.Extractor import Extractor


class PdfExtractor(Extractor):
    def __init__(self, address: str):
        super().__init__(address=address)

        self.file_path = address

    def __extract_data(self) -> str:
        fake_file_handle = io.StringIO()
        resource_manager = PDFResourceManager()

        try:
            converter = TextConverter(resource_manager, fake_file_handle)
            page_interpreter = PDFPageInterpreter(resource_manager, converter)

        except Exception as e:
            exception(msg=f'Failed while trying init Converters objects: {e}')
            return ''

        with open(self.file_path, 'rb') as file:
            [page_interpreter.process_page(page) for page in
            PDFPage.get_pages(file, caching=True, check_extractable=True)]

            text = fake_file_handle.getvalue()

        converter.close()
        fake_file_handle.close()

        return text

    def extract_text_from_file(self) -> str:
        return self.__extract_data()
