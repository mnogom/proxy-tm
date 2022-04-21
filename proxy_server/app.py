from flask import Flask, request
from requests import Session
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import re

app = Flask(__name__)

BASE_URL = 'https://news.ycombinator.com'
session = Session()


@app.route('/')
@app.route('/<path:_>')
def get_page(**kwargs):
    uri = request.environ.get('RAW_URI')
    response = session.get(urljoin(BASE_URL, uri))

    if response.headers.get('content-type').find('text/html') != -1:

        soup = BeautifulSoup(response.text)
        for tag in soup.find_all(text=True):
            current_string = tag.get_text()
            if current_string:
                modified_string = re.sub(r'(\b[A-Za-z]{6}\b)', '\g<1>™', current_string)
                tag.replace_with(modified_string)

        return soup.prettify()
    return response.content


if __name__ == '__main__':
    app.run()
