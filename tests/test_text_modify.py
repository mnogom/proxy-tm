import pytest
from proxy_server.content_modifier import _add_tm


@pytest.mark.parametrize('input, expected',
                         [('Search:', 'Search™:'),
                          ('letter', 'letter™'),
                          ('(~yellow)', '(~yellow™)'),
                          ('C2H5OH', 'C2H5OH'),
                          ('C6H5CH2OH', 'C6H5CH2OH'),
                          ('(~all)', '(~all)'),
                          ('shiny…', 'shiny…'),
                          ('aren\'t', 'aren\'t'),
                          ('Applications', 'Applications')])
def test_add_tm(input, expected):
    assert _add_tm(input) == expected
