#!/usr/bin/env python3

import os
import re


def make_name(url):
    '''Modifies the url for naming'''
    print(url)
    url_root, ext = os.path.splitext(url)
    print(url_root, ext)
    url_no_scheme = url_root.split('://')[1]
    url_no_symb = re.sub('[^a-zA-Z0-9]', '-', url_no_scheme)
    return url_no_symb


def make_file_name(url, file_ext='.html'):
    '''Makes a name for a new html file'''
    url_root, ext = os.path.splitext(url)
    if ext == '':
        ext = '.html'
    file_ext = ext
    file_root = make_name(url)
    file_name = file_root + file_ext
    return (file_name, ext)


def create_named_dir(url, path):
    '''Creates a directory for content'''
    dir_root = make_name(url)
    dir_name = dir_root + '_files'
    dir_path = os.path.join(path, dir_name)
    os.mkdir(dir_path)
    return dir_path
