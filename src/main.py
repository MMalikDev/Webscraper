from pprint import pprint
from typing import Dict, List, Union

import httpx

from configs import core, schema
from lib.crawl import crawl
from lib.output import save_db, save_json
from lib.parse import parse
from lib.scrape import scrape
from lib.utilities import debug


def webscapper(website: schema.Schema, show_data: bool) -> None:
    page = website.page
    url = website.url + page if website.page else website.url

    results = []
    for i in range(website.page_min, website.page_limit):
        site = url % i if page else url
        html = scrape(site, website.js_required, website.headers)
        nodes = parse(html, website.parent_nodes, website.child_nodes)
        content = [website.item(**node) for node in nodes]  #  Clean Data
        if not content:
            break
        results += content

    if show_data:
        pprint(results)

    data = [i.__dict__ for i in results]

    save_db(website.db, data)
    save_json(website.item.__name__, data)


def api_call(website: schema.Schema) -> Union[List[str], Dict[str, str]]:
    url = website.url + website.page
    results = []
    for i in range(website.page_min, website.page_limit):
        response = httpx.get(url % i)
        content: Union[Dict, List] = response.json()
        if website.key in content:
            content: Dict = content.get(website.key, content)
        if not content:
            break
        results += content
    return results


# ---------------------------------------------------------------------- #
# Main Functions                                                         #
# ---------------------------------------------------------------------- #
@debug
def main():
    website: schema.Schema = schema.schema

    if website.api:
        data = api_call(website)
        save_json("%s_api" % website.name, data)
    if website.crawl:
        data = crawl(website.url, not core.settings.SHOW_DATA)
        save_json("%s_urls" % website.name, data)
    if website.model:
        webscapper(website, core.settings.SHOW_DATA)


if __name__ == "__main__":
    main()
