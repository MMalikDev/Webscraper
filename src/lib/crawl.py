from collections import defaultdict
from typing import Any, DefaultDict, Dict, List, Optional
from urllib.parse import urlparse

from playwright.sync_api import Request, Response, sync_playwright


def parse_url(url: str) -> Dict[str, str]:
    data = dict(url=url)
    parsed_url = urlparse(url)
    data["hostname"] = parsed_url.hostname
    data["path"] = parsed_url.path
    data["query"] = parsed_url.query
    return data


def get_requests(url: str, headless: bool) -> Dict[Request, Optional[Response]]:
    requests: List[Request] = []
    responses: List[Response] = []

    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=headless)
        page = browser.new_page()
        page.on("request", lambda request: requests.append(request))
        page.on("response", lambda response: responses.append(response))
        page.goto(url)
        browser.close()

    content = dict()
    for request in requests:
        content[request] = None
    for response in responses:
        content[response.request] = response
    return content


def get_status(requests: Dict[Request, Optional[Response]]) -> List[Optional[str]]:
    data = {}
    for request, response in requests.items():
        data[request.url] = response.status if response else None
    return data


def get_request_details(request: Request) -> Dict[str, str]:
    data = parse_url(request.url)
    data["method"] = request.method
    data["params"] = request.post_data
    data["type"] = request.resource_type
    data["headers"] = request.headers
    return data


def get_response_details(response: Optional[Response]) -> Optional[Dict[str, str]]:
    if response is None:
        return

    data = dict(status=response.status)
    data["headers"] = response.headers
    return data


def get_details(content: Dict[Request, Optional[Response]]) -> DefaultDict[str, list]:
    urls = defaultdict(list)
    for request, response in content.items():
        data = get_request_details(request)
        data["response"] = get_response_details(response)
        hostname = data.pop("hostname")
        urls[hostname].append(data)
    return urls


def crawl(url: str, headless: bool = True) -> Dict[str, Any]:
    content = get_requests(url, headless)
    data = parse_url(url)
    data["status"] = get_status(content)
    data["details"] = get_details(content)
    return data
