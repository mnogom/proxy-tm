import pytest
from proxy_server.content_modifier import _add_tm

INPUT_TASK_TEXT = ('The visual description of the colliding files, at '
                   'http://shattered.io/static/pdf_format.png, is not very helpful '
                   'in understanding how they produced the PDFs, so I took apart '
                   'the PDFs and worked it out.'
                   ''
                   'Basically, each PDF contains a single large (421,385-byte) JPG '
                   'image, followed by a few PDF commands to display the JPG. The '
                   'collision lives entirely in the JPG data - the PDF format is '
                   'merely incidental here. Extracting out the two images shows two '
                   'JPG files with different contents (but different SHA-1 hashes '
                   'since the necessary prefix is missing). Each PDF consists of a '
                   'common prefix (which contains the PDF header, JPG stream '
                   'descriptor and some JPG headers), and a common suffix (containing '
                   'image data and PDF display commands).')

EXPECTED_TASK_TEXT = ('The visual™ description of the colliding files, at '
                      'http://shattered.io/static/pdf_format.png, is not very helpful '
                      'in understanding how they produced the PDFs, so I took apart '
                      'the PDFs and worked™ it out.'
                      ''
                      'Basically, each PDF contains a single™ large (421,385-byte) JPG '
                      'image, followed by a few PDF commands to display the JPG. The '
                      'collision lives entirely in the JPG data - the PDF format™ is '
                      'merely™ incidental here. Extracting out the two images™ shows two '
                      'JPG files with different contents (but different SHA-1 hashes™ '
                      'since the necessary prefix™ is missing). Each PDF consists of a '
                      'common™ prefix™ (which contains the PDF header™, JPG stream™ '
                      'descriptor and some JPG headers), and a common™ suffix™ (containing '
                      'image data and PDF display commands).')


@pytest.mark.parametrize('input, expected',
                         [('Search:', 'Search™:'),
                          ('letter', 'letter™'),
                          ('(~yellow)', '(~yellow™)'),
                          ('C2H5OH', 'C2H5OH'),
                          ('C6H5CH2OH', 'C6H5CH2OH'),
                          ('(~all)', '(~all)'),
                          ('shiny…', 'shiny…'),
                          ('aren\'t', 'aren\'t'),
                          ('Applications', 'Applications'),
                          ('some-letter', 'some-letter'),
                          ('wouldn\'t', 'wouldn\'t'),
                          ('github.com', 'github.com'),
                          ('github.com/', 'github.com/'),
                          ('www.github.com/', 'www.github.com/'),
                          ('http://github.com', 'http://github.com'),
                          ('https://github.com', 'https://github.com'),
                          ('https://github.com/mnogom', 'https://github.com/mnogom'),
                          (INPUT_TASK_TEXT, EXPECTED_TASK_TEXT), ])
def test_add_tm(input, expected):
    assert _add_tm(input) == expected
