#!/usr/bin/env/python3

import argparse
import requests
import sys
import os
from page_loader.loader import download


DESCRIPTION = "downloads a web page and saves it in a dictory"
DIRECTORY_DESCR = 'set path to the output directory (default: directory of launch)'  # noqa E501

exceptions = (
    requests.ConnectionError,
    PermissionError,
    FileNotFoundError,
    OSError)


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
    try:
        file_path = download(args.url, args.output)
    except exceptions:
        sys.exit(1)
    print(file_path)


if __name__ == '__main__':
    main()
