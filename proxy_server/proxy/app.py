"""Entry point."""

from urllib.parse import urljoin

from flask import Flask, request
from requests import Session
from bs4 import BeautifulSoup
import logging

from proxy_server.content_modifier import modify_content
from proxy_server.asset_parser import modify_resources
from proxy_server.logger import get_logger
from proxy_server import settings

app = Flask(__name__)
app.config.from_object(settings)

session = Session()
get_logger()


@app.route('/', methods=('GET', 'POST', 'DELETE'))
@app.route('/<path:path>', methods=('GET', 'POST', 'DELETE'))
def get_page(**kwargs):
    """Main function."""

    logging.info(f'get request to {request.url}')

    path = request.path
    proxy_url = app.config.get('PROXY_URL')
    url = urljoin(proxy_url, path)
    response = session.request(method=request.method,
                               url=url,
                               data=request.data)
    response_content_type = response.headers.get('content-type')
    logging.info(f'get response with content type: {response_content_type}')

    if response_content_type.find('text/html') != -1:
        soup = BeautifulSoup(response.text,
                             features='html.parser')
        soup = modify_content(soup)
        print(request.base_url)
        soup = modify_resources(soup, proxy_url, request.base_url)
        return soup.prettify()
    return response.content
