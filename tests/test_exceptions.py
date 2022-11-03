#!/usr/bin/env python3

import pytest
import tempfile
import requests
import requests_mock
from page_loader.loader import download

BAD_URL = 'http://bad-test-page.com'
URL = 'https://test-page.com'


@pytest.fixture
def fake_source(requests_mock):
    requests_mock.get(BAD_URL, text='', status_code=404)
    requests_mock.get(URL, text='')

def test_status_code(fake_source):
    with tempfile.TemporaryDirectory() as tmpdir:
        with pytest.raises(requests.HTTPError):
            file_path = download(BAD_URL, tmpdir)


def test_connection():
    with tempfile.TemporaryDirectory() as tmpdir:
        with requests_mock.Mocker() as m:
            m.register_uri('GET', URL, exc=requests.ConnectionError)
            with pytest.raises(requests.ConnectionError):
                file_path = download(URL, tmpdir)

