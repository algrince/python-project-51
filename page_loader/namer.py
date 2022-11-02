#!/usr/bin/env python3

import os
import re

permitted = {'.png', '.jpeg', '.css', '.js'}

exts = {'img': '.png',
        'script': '.js',
        'link': '.html'}


def make_name(url, primary_file=True): # primary file: html or folder 
    '''Modifies the url for naming'''
    if primary_file is False:
        url_root, url_ext = os.path.splitext(url)
    else:
        url_root = url
    url_no_scheme = url_root.split('://')[1]
    url_no_symb = re.sub('[^a-zA-Z0-9]', '-', url_no_scheme)
    return url_no_symb.rstrip('-')


def make_file_name(url, tag='link',
                    primary_file=True):
    '''Makes a name for a new html file'''
    url_root, ext = os.path.splitext(url)
    file_ext = make_ext(ext, tag)
    file_root = make_name(url, primary_file)
    file_name = file_root + file_ext
    return (file_name, ext)


def make_ext(ext, tag):
    if ext == '' or ext not in permitted:
        return exts[tag]
        

def create_named_dir(url, path):
    '''Creates a directory for content'''
    dir_root = make_name(url)
    dir_name = dir_root + '_files'
    dir_path = os.path.join(path, dir_name)
    os.mkdir(dir_path)
    return dir_path
