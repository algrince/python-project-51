#!/usr/bin/env python3

from page_loader.page_loader import download, make_file_name
import os
import tempfile
import requests
import requests_mock


TEST_URL = 'https://test.page/project'
EXPECTED_FILE = 'test-page-project.html'

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


def test_download():
    fixture_path = './tests/fixtures/expected_file.html'
    with open(fixture_path, 'r') as f:
        fixture = f.read()
    with requests_mock.Mocker() as m:
        m.get(TEST_URL, text=fixture)
        with tempfile.TemporaryDirectory() as tmpdir:
            file_path = download(TEST_URL, tmpdir)
            expected_path = os.path.join(tmpdir, EXPECTED_FILE)

            assert expected_path == file_path

            with open(file_path, 'r') as d:
                downloaded = d.read()

                assert fixture == downloaded

