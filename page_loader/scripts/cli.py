#!/usr/bin/env/python3

import argparse
import os
from page_loader.loader import download


DESCRIPTION = "downloads a web page and saves it in a dictory"
DIRECTORY_DESCR = 'set path to the output directory (default: directory of launch)'  # noqa E501


parser = argparse.ArgumentParser(description=DESCRIPTION)
parser.add_argument(
    '-o', '--output',
    default=os.getcwd(),
    help=DIRECTORY_DESCR
)
parser.add_argument(
    'url',
    type=str,
    metavar='PAGE',
    help='url of page to download'
)


def main():
    args = parser.parse_args()
    file_path = download(args.url, args.output)
    print(file_path)


if __name__ == '__main__':
    main()
