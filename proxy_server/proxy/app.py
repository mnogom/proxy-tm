"""Entry point."""

from urllib.parse import urljoin

from flask import Flask, make_response, request
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

    path = request.environ.get('RAW_URI')
    proxy_url = app.config.get('PROXY_URL')
    url = urljoin(proxy_url, path)
    response = session.request(method=request.method,
                               url=url,
                               data=request.data)
    response_content_type = response.headers.get('Content-Type')
    logging.info(f'get response with content type: {response_content_type}')

    if any([response_content_type.find('text/html') != -1,
            response_content_type.find('text/plain') != -1]):
        soup = BeautifulSoup(response.text,
                             features='html.parser')
        soup = modify_content(soup)
        soup = modify_resources(soup, proxy_url, request.base_url)
        content = str(soup)
    else:
        content = response.content

    print(response.headers.items())
    proxy_response = make_response(content, response.status_code)
    proxy_response.headers = {'Content-Type': response_content_type}
    return proxy_response
