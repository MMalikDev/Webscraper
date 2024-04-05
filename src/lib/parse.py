from collections import namedtuple
from typing import Dict, List, Optional

from selectolax.parser import HTMLParser, Node

Configs = namedtuple("Configs", ["selector", "attribute"])
Nodes = List[Dict[str, Optional[str]]]


def get_attribute(node: Node, selector: str, attribute: str) -> Optional[str]:
    match attribute:
        case "text":
            return node.css_first(selector).text(strip=True)
        case _:
            return node.css_first(selector).attributes.get(attribute, "")


def get_children(children: List[Node], hashmap: Dict[str, Configs]) -> Nodes:
    nodes = []
    for child in children:
        node = {}
        for k, v in hashmap.items():
            node[k] = get_attribute(child, v.selector, v.attribute)
        nodes.append(node)
    return nodes


def parse(
    html: HTMLParser, parent: Dict[str, str], children: Dict[str, Dict[str, str]]
) -> Nodes:
    articles = html.css(parent.get("css", "*"))
    children = {
        k: Configs(v.get("css", "*"), v.get("attribute", "text"))
        for k, v in children.items()
    }

    return get_children(articles, children)
