from pathlib import Path
from typing import Optional
from urllib.parse import urlparse

import httpx
from playwright.sync_api import sync_playwright
from selectolax.parser import HTMLParser

from lib.output import save_file


def trim_url(url: str) -> str:
    parsed_url = urlparse(url)
    return "data/websites/%s/%s/%s.response" % (
        parsed_url.hostname,
        parsed_url.path,
        parsed_url.query,
    )


def use_webdriver(url: str) -> str:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(url)
        content = page.content()
        browser.close()
    return content


def use_local_file(filename: str) -> str:
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
    return content


def scrape(
    url: str, js_required: bool = False, headers: Optional[httpx.Headers] = None
) -> HTMLParser:
    filename = trim_url(url)

    if Path(filename).is_file():
        content = use_local_file(filename)
    elif js_required:
        content = use_webdriver(url)
        save_file(filename, content)
    else:
        content = httpx.get(url, headers=headers).text
        save_file(filename, content)

    return HTMLParser(content)
