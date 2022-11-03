#!/usr/bin/env python3

from page_loader.source_changer import check_domain, check_src

TEST_URL = 'https://test-page.com'


def test_absolute_src():
    abs_src = TEST_URL
    rel_src = 'www.test.com'
    rel_src2 = 'test.com'
    null_src = ''

    assert check_src(abs_src) is True
    assert check_src(rel_src) is False
    assert check_src(rel_src2) is False
    assert check_src(null_src) is False


def test_domain():
    src_eq = 'https://test-page.com/content.png'
    src_diff = 'https://not-test-page.com/content.png'
    src_not_abs = '/asserts/content.png'
    src_diff_dom = 'https://test-page.org/content.png'

    joined = 'https://test-page.com/asserts/content.png'

    assert check_domain(TEST_URL, src_eq) == src_eq
    assert check_domain(TEST_URL, src_diff) is None
    assert check_domain(TEST_URL, src_diff_dom) is None
    assert check_domain(TEST_URL, src_not_abs) == joined
