#!/usr/bin/env python3

from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
from page_loader.namer import make_file_name, create_named_dir
from page_loader.source_changer import check_domain, replace_src
import requests
import os
import re


default_path = os.getcwd()

exts = {'img': '.png',
        'script': '.js',
        'link': 'link'}

contents = [('img', 'src'),
            ('script', 'src'),
            ('link', 'href')]



def download(url, path=default_path):
    '''Dowloands the page as html file (prettyfied by BS)'''
    file_name = make_file_name(url)
    output_path = os.path.join(path, file_name)
    with open(output_path, 'w') as output_file:
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')
        paths = [path, output_path]
        soup_changed = save_content(url, paths, soup)
        output_file.write(soup_changed.prettify())
    return output_path


def download_cnt(sources, paths, types):
    '''Dowloads and saves as a  file an image'''
    scr, src_url = sources
    tag = types[0]
    folder_path = paths[1]
    cnt_file_name = make_file_name(src_url, file_ext=exts[tag])
    cnt_output_path = os.path.join(folder_path, cnt_file_name)
    mode = choose_mode(tag)
    with open(cnt_output_path, mode) as cnt_file:
        cnt = requests.get(src_url)
        cnt_file.write(cnt.content)
    return cnt_output_path


def choose_mode(tag):
    '''Choses a write mode for a file'''
    return 'wb' if tag == 'img' else 'w'


def save_content(url, paths, soup):
    '''Saves additional content from the page'''
    root_path = paths[0]
    folder_path = create_named_dir(url, root_path)
    print(soup)
    for content in contents:
        # print(soup)
        # soup = scrape_content(content, soup, paths)
        type_, attribute = content
        tabs = soup.find_all(type_)
        for tab in tabs:
            source = tab[attribute]
            source_url = check_domain(url, source)
            if source_url is None:
                continue
            else:
                sources = [source, source_url]
                cnt_output_path = download_cnt(
                    sources,
                    paths,
                    types
                )
                soup = replace_src(
                    soup, 
                    cnt_output_path, 
                    source,
                    types)
    return soup


'''def scrape_content(types, soup, paths):
    Scrapes content from the page
    print(soup)
    type_, attribute = types
    tabs = soup.find_all(type_)
    for tab in tabs:
        source = tab[attribute]
        source_url = check_domain(url, source)
        if source_url is None:
            continue
        else:
            sources = [source, source_url]
            cnt_output_path = download_cnt(
                sources,
                paths,
                types
            )
            soup = replace_src(
                soup, 
                cnt_output_path, 
                source,
                types)
        return soup'''
