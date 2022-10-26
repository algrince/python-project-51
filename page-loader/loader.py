#ª/usr/bin/env python3

import requests
import os
import re


default_path = os.getcwd()

def download(url, path=default_path):
    file_name = make_file_name(url)
    output_path = os.path.join(path, file_name)
    return output_path

def make_file_name(url):
    url_root, ext = os.path.splitext(url)
    url_wo_scheme = url_root.split(':')[1]
    url_with_symb = url_with_symb[2:]
    url_wo_symb = re.sub('[^a-zA-Z0-9]', '-', url_with_symb)
    file_name = add_ext(url_wo_symb)
    return file_name


def add_ext(root):
    file_ext = '.html'
    if root[-5:] == file_ext:
        return root
    else: 
        return root + file_ext
