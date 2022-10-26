#!/usr/bin/env/python3

import argparse
import os


DESCRIPTION = "downloads a web page and saves it in a dictory"
DIRECTORY_DESCR = 'set path to the output directory (default: directory of launch)' 


parser = argparse.ArgumentParser(description=DESCRIPTION)
parser.add_argument(
        '-o', '--output',
        metavar='DIRECTORY',
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
    pass

if __name__ == '__main__':
    main()
