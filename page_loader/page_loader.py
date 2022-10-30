#!/usr/bin/env python3

from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
from page_loader.namer import make_file_name, create_named_dir
import requests
import os
import re


default_path = os.getcwd()


def download(url, path=default_path):
    '''Dowloands the page as html file (prettyfied by BS)'''
    file_name = make_file_name(url)
    output_path = os.path.join(path, file_name)
    with open(output_path, 'w') as output_file:
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')
        soup_changed = save_content(url, path, output_path, soup)
        output_file.write(soup_changed.prettify())
    return output_path


def save_content(url, path, output_path, soup):
    '''Saves additional content from the page'''
    folder_path = create_named_dir(url, path)
    images = soup.find_all('img')
    for image in images:
        src = image['src']
        src_url = check_domain(url, src)
        if src_url is None:
            continue
        else:
            img_output_path = download_img(
                src, src_url,
                folder_path,
                output_path
            )
            soup = replace_src(soup, img_output_path, src)
    return soup


def download_img(src, src_url, folder_path, output_path):
    '''Dowloads and saves as a png file an image'''
    img_f_name = make_file_name(src_url, file_ext='.png')
    img_output_path = os.path.join(folder_path, img_f_name)
    with open(img_output_path, 'wb') as img_file:
        img = requests.get(src_url)
        img_file.write(img.content)
    return img_output_path


def replace_src(soup, img_output_path, orig_src):
    '''Replaces src'''
    tag = soup.find('img', src=orig_src)
    tag['src'] = img_output_path
    return soup


def check_domain(url, src):
    '''Checks that content belongs to the same domain and if it is abolute'''
    url_parse = urlparse(url)
    url_netloc = url_parse.netloc
    src_netloc = urlparse(src).netloc
    if url_netloc == src_netloc:
        return src
    else:
        is_absolute = check_src(src)
        if is_absolute:
            return None
        else:
            joined_src = urljoin(url, src)
            return joined_src


def check_src(src):
    '''Checks if src link is absolute'''
    match = re.search('^http', src)
    return False if match is None else True
