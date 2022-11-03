#!/usr/bin/env python3

from page_loader.namer import make_name, make_file_name, create_named_dir
import tempfile


GENERIC_URL = 'https://docs.python.org/3/library/re.html'


def test_filename_maker():
    url1 = 'https://ru.hexlet.io/projects/51/members/25821'
    file1 = 'ru-hexlet-io-projects-51-members-25821.html'
    url2 = 'https://ci3.googleusercontent.com/proxy/cutloads/290832164/md_1809631.png'
    file2 = 'ci3-googleusercontent-com-proxy-cutloads-290832164-md-1809631.png'
    url3 = 'https://github.com/'
    file3 = 'github-com.html'

    assert make_file_name(url1)[0] == file1
    assert make_file_name(url2)[0] == file2
    assert make_file_name(url3)[0] == file3


def test_name_maker():
    url_symb = 'https://www.google.com/search?q=patata&oq=patata&aqs=chrome' # noqa
    url_output1 = 'www-google-com-search-q-patata-oq-patata-aqs-chrome' # noqa
    url_normal = GENERIC_URL
    url_output2 = 'docs-python-org-3-library-re'

    assert make_name(url_symb) == url_output1
    assert make_name(url_normal) == url_output2


def test_named_dir_creator():
    with tempfile.TemporaryDirectory() as tmpdir:
        expected_path = 'docs-python-org-3-library-re-html_files'
        dir_path = create_named_dir(GENERIC_URL, tmpdir)[0]

        assert dir_path == expected_path
