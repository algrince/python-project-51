#!/usr/bin/env python3

from page_loader.page_loader import download, make_file_name
import os
import tempfile
import requests
import requests_mock


TEST_URL = 'https://test.page/project'
EXPECTED_FILE = 'test-page-project.html'


def test_download():
    fixture_path = './tests/fixtures/source_file.html'
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

