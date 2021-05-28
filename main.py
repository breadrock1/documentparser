from typing import Dict
from json import dump
from pathlib import Path
from logging import info, warn
from argparse import ArgumentParser, Namespace

from Parsers.PdfParser import PdfParser
from Parsers.DocParser import DocParser


def __writeOutResults(output_dir: str, data: Dict) -> None:
    def generate_filename() -> str:
        return f'{output_dir}/users.json'

    with open(generate_filename(), 'w+') as file:
        dump(
            data,
            file,
            indent=4,
            sort_keys=False
        )
        file.close()


def __parseDocument(args: Namespace) -> None:
    info(msg='[+]\tStarting parsing document process...')

    path_to_file = args.f
    path_to_output_file = args.o

    extension = Path(path_to_file).suffix

    if extension == ".pdf":
        text_data = PdfParser.extract_text_from_file(path_to_file)
    elif extension == ".doc" or extension == ".docx":
        text_data = DocParser.extract_text_from_file(path_to_file)
    else:
        warn(msg='Unknown file extension. Please check the extension is correct!')
        return

    __writeOutResults(path_to_output_file, text_data)
    info(msg='[+]\tThe scraping process has been done!')


if __name__ == '__main__':
    argumentParser = ArgumentParser(
        prog='DocumentParser',
        usage='''
                ./simple_run.py {-f --document-file} [-o --output-file] 
            ''',
        description='''
                This python script automate process of parsing information from documents like pdf and doc(x)
            ''',
        add_help=True,
        allow_abbrev=True
    )

    argumentParser.add_argument(
        '-f', metavar='--document-file', type=str, required=True,
        help='Specify path to document file.'
    )
    argumentParser.add_argument(
        '-o', metavar='--output-file', type=str, required=False,
        help='Specify path to output file.',
        default=str(Path() / 'Results')
    )

    arguments = argumentParser.parse_args()
    __parseDocument(args=arguments)
