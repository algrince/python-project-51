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
        output_file.write(soup.prettify())
    save_content(url, path, soup)
    return output_path


def save_content(url, path, soup):
    '''Saves additional content from the page'''
    folder_path = create_named_dir(url, path)
    images = soup.find_all('img')
    for image in images:
        src = image['src']
        src_url = check_domain(url, src)
        if src_url is None:
            continue
        else:
            img_output_path = dowload_img(src_url, folder_path)
            

def dowload_img(src_url, folder_path):
    '''Dowloads and saves as a png file an image'''
    img_f_name = make_file_name(src_url, file_ext='.png')
    img_output_path = os.path.join(folder_path, img_f_name)
    with open(img_output_path, 'wb') as img_file:
        img = requests.get(src_url)
        content_file.write(img.content)
    return img_output_path


def replace_src(file_path, img_output_path, orig_src):
    '''Replaces src'''
    with open(file_path, 'w') as f:
        base_file = f.read()
        tag = base_file.find('img', src=orig_src)
        tag['src'] = img_output_path    


def check_domain(url, src):
    '''Checks that content belongs to the same domain and if it is abolute'''
    url_parse = urlparse(url)
    url_netloc = url_parse.netloc
    url_scheme = url_parse.scheme
    src_netloc = urlparse(src).netloc
    if url_netloc == src_netloc:
        return src
    else:
        is_absolute = check_src(src)
        if is_absolute:
            return None
        else:
            url_base = url_scheme + '://' + url_netloc
            joined_src = urljoin(url_base, src)
            return joined_src


def check_src(src):
    '''Checks if src link is absolute'''
    match = re.search('^http', src)
    return False if match is None else True
