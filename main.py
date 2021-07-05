from json import dump
from typing import Dict
from pathlib import Path
from argparse import ArgumentParser, Namespace

from Main.ParserManager import ParserManager


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


def __launchParsingWebpages(args: Namespace) -> None:
    text_data = ParserManager.parseWebpage(link_to_webpage=args.f)
    __writeOutResults(output_dir=args.o, data=text_data)


def __launchParsingDocuments(args: Namespace) -> None:
    text_data = ParserManager.parseDocument(path_to_file=args.f)
    __writeOutResults(output_dir=args.o, data=text_data)


if __name__ == '__main__':
    argumentParser = ArgumentParser(
        prog='DocumentParser',
        usage='''
                ./simple_run.py {-f --document-file} {-w --web-page} [-o --output-file] 
            ''',
        description='''
                This python script automate process of parsing information from documents 
                like pdf and doc(x) or webpage by link
            ''',
        add_help=True,
        allow_abbrev=True
    )

    argumentParser.add_argument(
        '-f', metavar='--document-file', type=str, required=True,
        help='Specify path to document file.'
    )
    argumentParser.add_argument(
        '-w', metavar='--web-page', type=str, required=True,
        help='Specify link to webpage.'
    )
    argumentParser.add_argument(
        '-o', metavar='--output-file', type=str, required=False,
        help='Specify path to output file.',
        default=str(Path() / 'Results')
    )

    __launchParsingDocuments(argumentParser.parse_args())
