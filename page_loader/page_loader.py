#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests
import os
import re


default_path = os.getcwd()


def download(url, path=default_path):
    '''Dowloands the page as html file (prettyfied by BS)'''
    file_name = make_file_name(url)
    output_path = os.path.join(path, file_name)
    with open(output_path, 'w') as output_file:
        page = requests.get(url).text
        soup = BeautifulSoup(page, 'html.parser')
        output_file.write(soup.prettify())
    return output_path


def save_content(url, file_path):
    '''Saves additional content from the page'''
    folder_path = create_named_dir(url, file_path)
    save_img(file_path, folder_path)


def save_img(file_path, folder_path):
    pass


def make_name(url):
    '''Modifies the url for naming'''
    url_root, ext = os.path.splitext(url)
    url_wo_scheme = url_root.split(':')[1]
    url_with_symb = url_wo_scheme[2:]
    url_wo_symb = re.sub('[^a-zA-Z0-9]', '-', url_with_symb)
    return url_wo_symb


def make_file_name(url):
    '''Makes a name for a new html file'''
    file_root = make_name(url)
    file_ext = '.html'
    file_name = file_root + file_ext
    return file_name


def create_named_dir(url, path):
    '''Creates a directory for content'''
    dir_root = make_name(url)
    dir_name = dir_root + '_files'
    dir_path = os.path.join(path, dir_name)
    os.mkdir(dir_path)
    return dir_path
