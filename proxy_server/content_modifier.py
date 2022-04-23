"""Content modifier."""

import re
import logging

ADDITIONAL_TAGS = {
    'img': ('alt',),
    'input': ('value', 'placeholder',),
}


SIX_LETTERS_PATTERN = r'(\b[A-Za-z]{6}\b)'
PATTERNS_TO_AVOID = {
    # https://stackoverflow.com/a/48769624
    'url': r'(?:(?:https?|ftp):\/\/)?[\w/\-?=%.]+\.[\w/\-&?=%.]+',
    'hyphens_apostrophes': r'\b\w*[-\']\w*\b',
}


def _is_match_avoiding_patterns(word):
    """Check if word matches with any pattern for avoiding."""
    return any(re.match(pattern, word)
               for pattern in PATTERNS_TO_AVOID.values())


def _add_tm(input_string: str) -> str:
    """Insert after every word with 6 letters symbol ™.
    :param text: text with words to modify
    :return: modify copy of input text
    """

    output_string = []
    for word in input_string.split(' '):
        if _is_match_avoiding_patterns(word):
            output_string.append(word)
        else:
            output_string.append(re.sub(SIX_LETTERS_PATTERN, r'\g<1>™', word))
    return ' '.join(output_string)


def _modify_custom_attrs(soup):
    """Modify custom attributes in HTML-tags.
    :param soup: BeautifulSoup object
    :return: Modified BeautifulSoup object
    """

    for tag, attrs in ADDITIONAL_TAGS.items():
        assets = soup.find_all(tag)
        for asset in assets:
            for attr in attrs:
                attr_value = asset.get(attr)
                if attr_value:
                    asset[attr] = _add_tm(attr_value)
    return soup


def _modify_text_content(soup):
    """Modify visible text on HTML-page.
    :param soup: BeautifulSoup object
    :return: Modified BeautifulSoup object
    """

    for tag in soup.find_all(string=True):
        current_string = tag.get_text()
        if current_string:
            modified_string = _add_tm(current_string)
            tag.replace_with(modified_string)
    return soup


def modify_content(soup):
    """Modify all visible text on HTML-page and
    modify custom attributes in HTML-tags.

    :param soup: BeautifulSoup object
    :return: BeautifulSoup object
    """

    soup = _modify_text_content(soup)
    soup = _modify_custom_attrs(soup)
    logging.info('Content was modified')
    return soup
