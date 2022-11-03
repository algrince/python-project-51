#!/usr/bin/env python3

from page_loader.logger import logging
import os
import re

permitted = {'.png', '.jpeg', '.css', '.js'}

exts = {'img': '.png',
        'script': '.js',
        'link': '.html'}


def make_name(url, primary_file=False):  # primary file: html
    '''Modifies the url for naming'''
    if primary_file:
        url_root = url
    else:
        url_root, url_ext = os.path.splitext(url)
    url_no_scheme = url_root.split('://')[1]
    url_no_symb = re.sub('[^a-zA-Z0-9]', '-', url_no_scheme)
    return url_no_symb.rstrip('-')


def make_file_name(url, tag='link', primary_file=False):
    '''Makes a name for a new html file'''
    url_root, ext = os.path.splitext(url)
    file_ext = make_ext(ext, tag)
    file_root = make_name(url, primary_file)
    file_name = file_root + file_ext
    return (file_name, ext)


def make_ext(ext, tag):
    if ext == '' or ext not in permitted:
        return exts[tag]
    else:
        return ext


def create_named_dir(url, path):
    '''Creates a directory for content'''
    dir_root = make_name(url, primary_file=True)
    dir_name = dir_root + '_files'
    dir_path = os.path.join(path, dir_name)
    try:
        os.mkdir(dir_path)
    except PermissionError as e:
        logging.error(f'Permission denied to make a directory {dir_path}')
        raise e
    except OSError as e:
        logging.error(e)
        raise e
    return [dir_name, dir_path]
