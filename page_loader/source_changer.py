#!/usr/bin/env python3


from urllib.parse import urlparse, urljoin
import re


def replace_src(soup, cnt_output_name, orig_src, types):
    '''Replaces src'''
    type_, atr = types
    if atr == 'href':
        tag = soup.find(type_, href=orig_src)
    else:
        tag = soup.find(type_, src=orig_src)
    try:
        tag[atr] = cnt_output_name
    except TypeError:
        pass
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
