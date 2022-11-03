#!/usr/bin/env python3

from bs4 import BeautifulSoup
from page_loader.loader import download, download_cnt, save_content
from urllib.parse import urljoin
import os
import shutil
import tempfile
import pytest
import requests_mock


URL = {
    'html': 'https://test-page.com',
    'image': 'https://test-page.com/assets/professions/python.png',
    'link1': 'https://test-page.com/assets/application.css',
    'link2': 'https://test-page.com/courses',
    'script': 'https://test-page.com/packs/js/runtime.js'
}


PATH = {
    'html': './tests/fixtures/full_fixture.html',
    'image': './tests/fixtures/python.png',
    'link1': './tests/fixtures/link1.css',
    'link2': './tests/fixtures/link2.html',
    'script': './tests/fixtures/script.js'
}

TEST_URL = 'https://test-page.com'
EXPECTED_FILE = 'test-page-com.html'

SOURCE = './tests/fixtures/source_file.html'
EXPECTED = './tests/fixtures/expected_file.html'

IMAGE = './tests/fixtures/python.png'

FULL_EXPECTED = './tests/fixtures/full_expected.html'


def test_path():
    fixture_path = SOURCE
    with open(fixture_path, 'r') as f:
        fixture = f.read()
    with requests_mock.Mocker() as m:
        m.get(URL['html'], text=fixture)
        with tempfile.TemporaryDirectory() as tmpdir:
            file_path = download(URL['html'], tmpdir)
            expected_path = os.path.join(tmpdir, EXPECTED_FILE)

            assert file_path == expected_path


def test_files():
    fixture_path = SOURCE
    with open(fixture_path, 'r') as f:
        fixture = f.read()
    with requests_mock.Mocker() as m:
        m.get(URL['html'], text=fixture)
        with tempfile.TemporaryDirectory() as tmpdir:
            file_path = download(URL['html'], tmpdir)
            with open(file_path, 'r') as d, open(EXPECTED, 'r') as e:
                downloaded = d.read()
                expected = e.read()

                assert downloaded == expected


def test_img_download():
    with open(IMAGE, 'rb') as f:
        png_fixture = f.read()
    with requests_mock.Mocker() as m:
        src = 'python.png'
        img_url = urljoin(URL['html'], src)
        m.get(img_url, content=png_fixture)
        with tempfile.TemporaryDirectory() as tmpdir:
            output_path = download_cnt(img_url, tmpdir, tmpdir, 'img')
            with open(output_path, 'rb') as d:
                downloaded_img = d.read()

                assert downloaded_img == png_fixture


@pytest.fixture
def fake_sources(requests_mock):
    requests_mock.get(URL['image'], content=open(PATH['image'], 'rb').read())
    requests_mock.get(URL['link1'], content=open(PATH['link1'], 'rb').read())
    requests_mock.get(URL['link2'], text=open(PATH['link2'], 'r').read())
    requests_mock.get(URL['script'], content=open(PATH['script'], 'rb').read())


def test_saver(fake_sources):
    with open(PATH['html'], 'r') as s:
        source_page = s.read()
        soup = BeautifulSoup(source_page, 'html.parser')
    with tempfile.TemporaryDirectory() as tmpdir:
        output_file_path = shutil.copy(PATH['html'], tmpdir)
        url = URL['html']
        paths = [tmpdir, output_file_path]
        folder = save_content(url, paths, soup)
        folder_path = os.path.join(tmpdir, folder)

        assert 4 == len(os.listdir(folder_path))

        with open(output_file_path, 'r') as new, open(FULL_EXPECTED, 'r') as exp:
            assert new.read() == exp.read()
