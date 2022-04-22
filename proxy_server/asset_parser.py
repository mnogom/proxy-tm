"""Asset parser."""

import logging
from urllib.parse import urlparse, urlunparse

ASSETS_TYPES = {
    'img': 'src',
    'script': 'src',
    'link': 'href',
    'a': 'href',
}


def modify_resources(soup, proxy_url: str, app_url: str):
    """Find and modify assets urls.

    :param soup: BeautifulSoup object
    :param proxy_url: url that proxied
    :param app_url: url of app
    """

    app_parsed_url = urlparse(app_url)
    proxy_parsed_url = urlparse(proxy_url)
    for tag, attr in ASSETS_TYPES.items():
        assets = soup.find_all(tag)
        for asset in assets:
            asset_url = asset.get(attr)
            if asset_url:
                asset_parsed_url = urlparse(asset_url)
                if asset_parsed_url.netloc == proxy_parsed_url.netloc:
                    asset[attr] = urlunparse(
                        asset_parsed_url._replace(
                            netloc=app_parsed_url.netloc))
    logging.info('Resources was modified')
    return soup
