#!/usr/bin/env python3

from page_loader.namer import make_name, make_file_name, create_named_dir
import tempfile
import os


GENERIC_URL = 'https://docs.python.org/3/library/re.html'


def test_filename_maker():
    url1 = 'https://ru.hexlet.io/projects/51/members/25821'
    file1 = 'ru-hexlet-io-projects-51-members-25821.html'
    url2 = GENERIC_URL
    file2 = 'docs-python-org-3-library-re.png'
    url3 = 'https://www.w3schools.com/python/ref_string_split.asp'
    file3 = 'www-w3schools-com-python-ref-string-split.html'

    assert file1 == make_file_name(url1)
    assert file2 == make_file_name(url2, file_ext='.png')
    assert file3 == make_file_name(url3)


def test_name_maker():
    url_symb = 'https://www.google.com/search?q=patata&oq=patata&aqs=chrome' # noqa
    url_output1 = 'www-google-com-search-q-patata-oq-patata-aqs-chrome' # noqa
    url_normal = GENERIC_URL
    url_output2 = 'docs-python-org-3-library-re'

    assert url_output1 == make_name(url_symb)
    assert url_output2 == make_name(url_normal)


def test_named_dir_creator():
    with tempfile.TemporaryDirectory() as tmpdir:
            expected_dir = 'docs-python-org-3-library-re_files'
            expected_path = os.path.join(tmpdir, expected_dir)
            dir_path = create_named_dir(GENERIC_URL, tmpdir)

            assert expected_path == dir_path
