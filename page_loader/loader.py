#!/usr/bin/env python3

from bs4 import BeautifulSoup
from page_loader.namer import make_file_name, create_named_dir
from page_loader.source_changer import check_domain, replace_src
from page_loader.logger import logging
import requests
import os


default_path = os.getcwd()


exts = {'img': '.png',
        'script': '.js',
        'link': 'link'}

contents = [('img', 'src'),
            ('script', 'src'),
            ('link', 'href')]


def download(url, path=default_path):
    '''Dowloands the page as html file (prettyfied by BS)'''
    logging.info(f' requested url: {url}')
    logging.info(f' output path: {path}')

    file_name = make_file_name(url, primary_file=True)[0]
    output_file_path = os.path.join(path, file_name)

    logging.info(f' write html file: {output_file_path}')

    with open(output_file_path, 'w') as output_file:
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')
        output_file.write(soup.prettify())

    logging.info(f' download complete: html file {output_file_path}')

    paths = [path, output_file_path]
    folder_name = save_content(url, paths, soup)  # noqa: F841

    logging.info(' download completed')
    return output_file_path


def save_content(  # noqa: C901
        url, paths, soup):
    '''Saves additional content from the page'''
    root_path, output_file_path = paths
    folder_name, folder_path = create_named_dir(url, root_path)

    for content in contents:
        type_, attribute = content
        tabs = soup.find_all(type_)
        for tab in tabs:

            try:
                source = tab[attribute]
                source_url = check_domain(url, source)
            except KeyError:
                logging.warning(f" found '{type_}' tag with no requiered attribute ('{attribute}'") # noqa
                source_url = None

            if source_url is None:
                continue
            else:
                cnt_output_name = download_cnt(
                    source_url,
                    folder_name,
                    folder_path,
                    type_
                )
                if cnt_output_name is not None:
                    soup = replace_src(
                        soup,
                        cnt_output_name,
                        source,
                        content)
        logging.info(f' download complete: {type_} content')

    with open(output_file_path, 'w') as output_file:
        output_file.write(soup.prettify())
    logging.info(f' html file {output_file_path} rewritten')
    return folder_name


def download_cnt(src_url, folder_name, folder_path, tag):
    '''Dowloads and saves content'''
    cnt_file_name, ext = make_file_name(src_url, tag)
    cnt_output_name = os.path.join(folder_name, cnt_file_name)
    cnt_output_path = os.path.join(folder_path, cnt_file_name)
    mode = choose_mode(ext)
    with open(cnt_output_path, mode) as cnt_file:
        try:
            cnt = requests.get(src_url)
        except requests.exceptions.InvalidSchema:
            return None
        try:
            cnt_file.write(cnt.content)
        except TypeError:
            pass
    return cnt_output_name


def choose_mode(ext):
    '''Choses a write mode for a file'''
    return 'w' if ext == '.html' else 'wb'
