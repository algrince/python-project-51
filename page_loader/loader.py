#!/usr/bin/env python3

import requests
import os
import re


default_path = os.getcwd()


def download(url, path=default_path):
    file_name = make_file_name(url)
    output_path = os.path.join(path, file_name)
    with open(output_path, 'w') as output_file:
        page = requests.get(url)
        output_file.write(page)
    return output_path


def make_file_name(url):
    url_root, ext = os.path.splitext(url)
    url_wo_scheme = url_root.split(':')[1]
    url_with_symb = url_wo_scheme[2:]
    url_wo_symb = re.sub('[^a-zA-Z0-9]', '-', url_with_symb)
    file_ext = '.html'
    file_name = url_wo_symb + file_ext
    return file_name
