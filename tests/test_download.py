#!/usr/bin/env python3

from page_loader.page_loader import download, download_img
from urllib.parse import urljoin
import os
import tempfile
import requests
import shutil
import requests_mock


TEST_URL = 'https://test.page/project'
EXPECTED_FILE = 'test-page-project.html'
SOURCE = './tests/fixtures/source_file.html'
EXPECTED = './tests/fixtures/expected_file.html'
IMG_FIXTURE = './tests/fixtures/img_fixture.html'

def test_path():
    fixture_path = SOURCE
    with open(fixture_path, 'r') as f:
        fixture = f.read()
    with requests_mock.Mocker() as m:
        m.get(TEST_URL, text=fixture)
        with tempfile.TemporaryDirectory() as tmpdir:
            file_path = download(TEST_URL, tmpdir)
            expected_path = os.path.join(tmpdir, EXPECTED_FILE)

            assert expected_path == file_path


def test_files():
    fixture_path = SOURCE
    with open(fixture_path, 'r') as f:
        fixture = f.read()
    with requests_mock.Mocker() as m:
        m.get(TEST_URL, text=fixture)
        with tempfile.TemporaryDirectory() as tmpdir:
            file_path = download(TEST_URL, tmpdir)
            with open(file_path, 'r') as d, open(EXPECTED, 'r') as e:
                downloaded = d.read()
                expected = e.read()

                assert expected == downloaded


def test_img_download():
    image = './tests/fixtures/python.png'
    with open(image, 'rb') as f:
        png_fixture = f.read()
    with requests_mock.Mocker() as m:
        src = 'python.png'
        img_url = urljoin(TEST_URL, src)
        m.get(img_url, content=png_fixture)
        with tempfile.TemporaryDirectory() as tmpdir:
            file_path = shutil.copy(IMG_FIXTURE, tmpdir)
            output_path = download_img(src, img_url, tmpdir, file_path)
            with open (output_path, 'rb') as d:
                downloaded_img = d.read()

                assert png_fixture == downloaded_img
