from bs4 import BeautifulSoup
from string import ascii_letters, digits
import re

inputs = ['Search:', 'C2H5OH', 'C6H5CH2OH', 'leTter', '(~all)', 'shiny…', '(~yellow)', 'aren\'t', 'Applications']
outputs = ['Search™:', 'C2H5OH', 'C6H5CH2OH', 'letter™', '(~all)', 'shiny…', '(~yellow™)', 'aren\'t', 'Applications']


def is_word(unparsed_word):
    return all(map(lambda x: x not in digits, unparsed_word))


def split_punctuation(unparsed_word):
    pass


if __name__ == '__main__':
    for word in inputs:
        print(re.findall(r'([A-Za-z]{6})', word))

    print('-' * 10)
    print(re.sub(r'(\b[A-Za-z]{6}\b)', '\g<1>™', ' '.join(inputs)))
