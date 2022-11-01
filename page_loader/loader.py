#!/usr/bin/env python3

from bs4 import BeautifulSoup
from page_loader.namer import make_file_name, create_named_dir
from page_loader.source_changer import check_domain, replace_src
import logging
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
    logging.info('requested url:')
    logging.info('output path:')

    file_name = make_file_name(url)[0]
    output_file_path = os.path.join(path, file_name)

    logging.info('write html file:')

    with open(output_file_path, 'w') as output_file:
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')
        paths = [path, output_file_path]
        soup_changed = save_content(url, paths, soup)
        output_file.write(soup_changed.prettify())
    return output_file_path


def download_cnt(sources, folder_path, types):
    '''Dowloads and saves as a  file an image'''
    scr, src_url = sources
    tag = types[0]
    cnt_file_name, ext = make_file_name(src_url, file_ext=exts[tag])
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
            print(cnt, src_url)
    return cnt_output_path


def choose_mode(ext):
    '''Choses a write mode for a file'''
    return 'w' if ext == '.html' else 'wb'


def save_content(url, paths, soup):
    '''Saves additional content from the page'''
    root_path = paths[0]
    folder_path = create_named_dir(url, root_path)
    for content in contents:
        type_, attribute = content
        tabs = soup.find_all(type_)
        for tab in tabs:
            try:
                source = tab[attribute]
                source_url = check_domain(url, source)
            except KeyError:
                source_url = None
            if source_url is None:
                continue
            else:
                sources = [source, source_url]
                cnt_output_path = download_cnt(
                    sources,
                    folder_path,
                    content
                )
                if cnt_output_path is not None:
                    soup = replace_src(
                        soup,
                        cnt_output_path,
                        source,
                        content)
    return soup