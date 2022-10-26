#!/usr/bin/env python3

from page_loader.loader import make_file_name


def test_name_maker():
    url1 = 'https://ru.hexlet.io/projects/51/members/25821'
    file1 = 'ru-hexlet-io-projects-51-members-25821.html'
    url2 = 'https://docs.python.org/3/library/re.html'
    file2 = 'docs-python-org-3-library-re.html'
    url3 = 'https://www.w3schools.com/python/ref_string_split.asp'
    file3 = 'www-w3schools-com-python-ref-string-split.html'

    assert file1 == make_file_name(url1)
    assert file2 == make_file_name(url2)
    assert file3 == make_file_name(url3)

